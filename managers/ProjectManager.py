from PyQt5 import QtCore
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper
from db import Query
from ui.project_leader_form import Ui_Form
from utils import info_boxes


class ProjectManager(QDialog, Ui_Form):
    def __init__(self, dbase, parent=None):
        super().__init__()
        self.setupUi(self)
        self.db = dbase
        self.parent = parent
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # destroy window object on close

        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("tblProjectManagers")
        self.new_index = None
        self.mapper = QDataWidgetMapper()
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.model.select()
        self.set_listview_items()
        self.mapper.setModel(self.model)
        self.set_mapping()
        self.mapper.toFirst()

        self.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.btn_edit.clicked.connect(self.on_btn_edit_clicked)
        self.btn_ok.clicked.connect(self.on_btn_submit_clicked)
        self.btn_remove.clicked.connect(self.are_related_tables)
        self.lstwg_manager.selectionModel().selectionChanged.connect(self.on_list_changed)
        self.deactivate_controls()
        if self.lstwg_manager.count() == 0:
            self.btn_edit.setEnabled(False)
            self.btn_remove.setEnabled(False)

    def set_mapping(self):
        self.mapper.addMapping(self.txt_name, self.model.fieldIndex('projectManager'))
        self.mapper.addMapping(self.txt_phone, self.model.fieldIndex('projectManagerPhone'))
        self.mapper.addMapping(self.txt_mail, self.model.fieldIndex('projectManagerMail'))

    def set_listview_items(self, row=0):
        self.lstwg_manager.clear()
        self.model.sort(1, Qt.AscendingOrder)
        if self.model.rowCount() > 0:
            for item in range(self.model.rowCount()):
                val = self.model.data(self.model.index(item, self.model.fieldIndex('projectManager')))
                self.lstwg_manager.addItem(val)

        self.lstwg_manager.setCurrentRow(row)

    def on_list_changed(self):
        if not self.btn_add.isEnabled():
            self.btn_add.setEnabled(True)
        if not self.btn_edit.isEnabled():
            self.btn_edit.setEnabled(True)
        if not self.btn_remove.isEnabled():
            self.btn_remove.setEnabled(True)
        row = self.lstwg_manager.currentRow()
        if row is not None:
            self.mapper.setCurrentModelIndex(self.model.index(row, 0))
            self.deactivate_controls()

    def deactivate_controls(self):
        self.btn_ok.setEnabled(False)
        self.txt_name.setReadOnly(True)
        self.txt_phone.setReadOnly(True)
        self.txt_mail.setReadOnly(True)
        self.lstwg_manager.setFocus()

    def activate_controls(self):
        self.btn_ok.setEnabled(True)
        self.txt_name.setReadOnly(False)
        self.txt_phone.setReadOnly(False)
        self.txt_mail.setReadOnly(False)
        self.lstwg_manager.setFocus()

    def on_btn_add_clicked(self):
        self.activate_controls()
        row = int(self.model.rowCount())
        self.model.insertRow(row)
        if self.new_index is None:
            self.new_index = QModelIndex(self.model.index(row, 0))
        self.mapper.setCurrentModelIndex(self.new_index)
        self.lstwg_manager.setCurrentIndex(self.new_index)
        self.lstwg_manager.setCurrentRow(self.new_index.row())
        self.btn_edit.setEnabled(False)
        self.btn_remove.setEnabled(False)
        self.txt_name.setFocus()

    def on_btn_edit_clicked(self):
        self.activate_controls()
        self.btn_add.setEnabled(False)
        self.btn_remove.setEnabled(False)
        self.txt_name.setFocus()

    def on_btn_submit_clicked(self):
        if self.validate_form([self.txt_name, self.txt_phone, self.txt_mail]):
            if self.new_index is not None:
                _row = self.new_index.row()
            else:
                _row = self.lstwg_manager.currentRow()
            if self.mapper.submit():
                self.model.select()
                self.set_listview_items(_row)
                self.new_index = None
            else:
                msg = self.model.lastError().text()
                if len(msg) > 0:
                    info_boxes.criticalBox("Błąd", msg)
                else:
                    info_boxes.criticalBox("Błąd", "Coś poszło nie tak")
        else:
            self.lstwg_manager.setCurrentRow(0)
        self.deactivate_controls()
        self.lstwg_manager.setFocus()

    def clear_all(self):
        self.txt_name.clear()
        self.txt_phone.clear()
        self.txt_mail.clear()

    def are_related_tables(self):
        row = self.lstwg_manager.selectionModel().currentIndex().row()
        current = self.model.data(self.model.index(row, self.model.fieldIndex('projectManager')))
        result = Query.are_related_records(self.db, 'tblProjects', 'projectManager', f'"{current}"')
        if result == 0:
            self.remove_data()
        else:
            info_boxes.criticalBox("Odmowa wykonania operacji",
                                   "Wybrana pozycja jest wykorzystana jako informacja w tabeli 'Zadania'")
        self.lstwg_manager.setFocus()

    def remove_data(self):
        if self.model.rowCount() > 0:
            row = self.lstwg_manager.currentIndex().row()
            response = info_boxes.questionBox('Usunięcie danych',
                                              'Czy na pewno chcesz trwale usunąć bieżący wiersz ?')
            if response == 16384:
                self.model.removeRow(row)
                self.set_listview_items(row - 1)
        self.lstwg_manager.setFocus()

    @staticmethod
    def validate_form(control_list):
        result = []
        for field in control_list:
            match field.__class__.__name__:
                case 'QComboBox':
                    if not field.currentText():
                        result.append(0)
                case 'QPlainTextEdit':
                    if not field.toPlainText():
                        result.append(0)
                case 'QDoubleSpinBox':
                    if field.value() == 0:
                        result.append(0)
                case 'QSpinBox':
                    if field.value() == 0:
                        result.append(0)
                case 'QLineEdit':
                    if not field.text():
                        result.append(0)
        if len(result) > 0:
            info_boxes.informationBox("Brak wymaganych informacji!",
                                      "Nie wszystkie wymagane pola zostały prawidłowo wypełnione.")
            return False
        else:
            return True

    def closeEvent(self, event):
        if self.parent.__class__.__name__ == 'TaskMapper':
            self.parent.cbo_manager.clear()
            self.parent.fill_combo(self.db, 'tblProjectManagers', 'projectManager', self.parent.cbo_manager)
        self.parent.project_manager = None