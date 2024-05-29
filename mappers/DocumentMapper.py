import os
import subprocess as sp
from PyQt5.QtCore import Qt, QEvent, QDate
from PyQt5.QtWidgets import QDialog
from mappers import Mapper
from ui.document_mapper import Ui_Form
from utils import file_io
from utils import info_boxes


class DocumentMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, index=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)
        Mapper.Mapper.__init__(self, manager, index, controls)
        self.setupUi(self)
        self.txt_info.installEventFilter(self)
        self.txt_document_sign.installEventFilter(self)
        self.btn_ok.clicked.connect(self.on_submit)
        self.btn_file.clicked.connect(self.add_file)
        self.btn_clear_file.clicked.connect(lambda: self.txt_file.clear())
        self.btn_copybook.clicked.connect(self.on_copybook)
        self.btn_restore.clicked.connect(self.on_restore)

        self.set_relation_field(["tblKeyDocumentCategories", "KeyDocumentCategoryID", "keyDocumentName"],
                                self.model.fieldIndex("keyDocumentName"),
                                self.cbo_document_name)
        self.cbo_document_name.model().sort(1, Qt.AscendingOrder)

        self.add_mapping(self.txt_document_sign, "keyDocumentSign")
        self.add_mapping(self.txt_info, "keyDocumentAdditionalInfo")
        self.add_mapping(self.dta_inflow, "keyDocumentObtainment")
        self.add_mapping(self.dta_document_issue, "keyDocumentDate")
        self.add_mapping(self.txt_file, "keyDocumentFile")

    def set_controls(self):
        self.cbo_document_name.setCurrentIndex(-1)
        self.dta_inflow.setDate(self.manager.current_date)
        self.dta_document_issue.setDate(self.manager.current_date)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if source is self.txt_info and (event.key() == Qt.Key.Key_Escape):
                cursor = self.txt_info.textCursor()
                cursor.insertText('Opłata miesięczna netto: ')
            if source is self.txt_document_sign and (event.key() == Qt.Key.Key_Escape):
                self.txt_document_sign.setText('Brak oznaczenia')
        return super(DocumentMapper, self).eventFilter(source, event)

    def on_submit(self):

        if self.validate_form([self.txt_document_sign, self.cbo_document_name]):

            if self.dta_document_issue.date() == self.manager.current_date:
                response = info_boxes.questionBox('Uwaga',
                                                  'Data dokumentu wskazuje na dzień dzisiejszy.\n Czy jest to poprawna informacja ?')
                if response != 16384:
                    return

            if self.mapper.submit():
                if not self.manager.parent.tabs_case_segments.isTabEnabled(1):
                    self.manager.parent.tabs_case_segments.setTabEnabled(1, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(1)
                self.btn_restore.setEnabled(False)
            else:
                self.model_last_error_msg()
                self.results.clear()
                self.results.append(self.dta_inflow.date().toString())
                self.results.append(self.dta_document_issue.date().toString())
                self.results.append(self.cbo_document_name.currentText())
                self.results.append(self.txt_document_sign.text())
                self.results.append(self.txt_info.toPlainText())
                self.results.append(self.txt_file.text())
                self.btn_restore.setEnabled(True)
            self.close()


    def on_restore(self):
       self.dta_inflow.setDate(QDate.fromString(self.results[0]))
       self.dta_document_issue.setDate(QDate.fromString(self.results[1]))
       self.cbo_document_name.setCurrentText(self.results[2])
       self.txt_document_sign.setText(self.results[3])
       self.txt_info.setPlainText(self.results[4])
       self.txt_file.setText(self.results[5])

    def add_file(self):
        path = self.manager.parent.settings[2] + '\\' + str(self.manager.current_row())
        name = file_io.get_file(path)
        file_name = name.split('/')[-1]
        self.txt_file.setText(file_name)

    def on_copybook(self):
        path = self.manager.parent.settings[0]
        programName = "notepad.exe"
        fileName = "notebook.txt"
        filePath = path + "\\" + fileName
        if os.path.isfile(filePath):
            sp.Popen([programName, filePath])
        else:
            info_boxes.informationBox('Informacja', f'Brak pliku: "{fileName}", w lokalizacji: "{path}"')