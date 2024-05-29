import ui.file_tag_generator
from PyQt5.QtWidgets import QDialog, QApplication
from utils import info_boxes
from db import Query


class DocumentTagGenerator(QDialog, ui.file_tag_generator.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.db = parent.manager.dbase
        self.doc_data = parent.generate_file_tag()
        self.doc_id = parent.get_document_id()
        self.btn_ok.clicked.connect(self.copy_to_clipboard)
        self.set_document_data()
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose) # destroy window object on close

    def set_document_data(self):
        self.cbx_extension.setChecked(True)
        if self.doc_data is None:
            info_boxes.criticalBox('Brak danych',
                                   'Brak aktualnego wiersza danych uniemożliwia wykonanie operacji.')
            return

        self.lbl_caption.setText(
            f'{self.doc_data[2]} | ({self.doc_data[0]}) | {self.doc_data[1]} | {self.doc_data[3]} | {self.doc_data[4]} | .pdf')
        self.doc_data[3] = self.doc_data[3].replace('/', '_').strip()
        self.doc_data[3] = self.doc_data[3].replace('\\', '_').strip()
        # self.doc_data[3] = self.doc_data[3].replace(' ', '_').strip()
        self.doc_data[4] = self.doc_data[4].strip()
        self.doc_data[2] = self.doc_data[2].strip()

        doc_file_tag = f'{self.doc_data[2]} ({self.doc_data[0]}) {self.doc_data[1]} {self.doc_data[3]} {self.doc_data[4]}.pdf'
        self.lbl_lenght.setText(f'Długość: {len(doc_file_tag) - 4} znaków')
        self.txt_file_tag.setText(doc_file_tag)

    def copy_to_clipboard(self):
        response = info_boxes.questionBox('Pytanie', 'Czy dodać wygenerowaną nazwę pliku do tabeli dokumentów ?')
        if response == 16384:
            if Query.update_value(self.db, 'tblKeyDocuments', 'keyDocumentFile', self.txt_file_tag.text(),
                                  'keyDocumentID', self.doc_id):
                info_boxes.informationBox('Aktualizacja danych',
                                          'Nazwa pliku została pomyślnie dodana do danych o dokumencie.')
            else:
                info_boxes.warningBox('Aktualizacja danych',
                                      'Niestety nazwa pliku nie została dodana do zbioru danych.')

        clipboard = QApplication.clipboard()
        if self.cbx_extension.isChecked():
            clipboard.setText(self.txt_file_tag.text())
        else:
            clipboard.setText(self.txt_file_tag.text()[:len(self.txt_file_tag.text()) - 4])

        self.close()