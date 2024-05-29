from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper
from db import Query
from ui.addressee_manager import Ui_Form
from utils import info_boxes


class AddresseeManager(QDialog, Ui_Form):
    def __init__(self, dbase, addressee_actions):
        super().__init__()
        self.setupUi(self)
        self.db = dbase

        if addressee_actions is not None:
            self.action_servants = addressee_actions[0]
            self.action_external = addressee_actions[1]
            self.action_internal = addressee_actions[2]

        self.model = QSqlTableModel(db=self.db)
        self.new_index = None
        self.mapper = QDataWidgetMapper()
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)

        if addressee_actions is not None:
            self.action_servants.triggered.connect(lambda: self.show_addressbook('servants'))
            self.action_external.triggered.connect(lambda: self.show_addressbook('external'))
            self.action_internal.triggered.connect(lambda: self.show_addressbook('internal'))

        self.btn_search.clicked.connect(self.on_search_clicked)
        self.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.btn_edit.clicked.connect(self.on_btn_edit_clicked)
        self.btn_ok.clicked.connect(self.on_btn_submit_clicked)
        self.btn_remove.clicked.connect(self.are_related_tables)
        self.lstvw_addressee.selectionModel().selectionChanged.connect(self.on_list_addressee_changed)

    def set_mapping(self):
        self.mapper.addMapping(self.txt_addresse_name, self.model.fieldIndex('addresseeName'))
        self.mapper.addMapping(self.fill_combo('tblStreets', 'streetName', self.cbo_addresse_street),
                               self.model.fieldIndex('addresseeStreet'))
        self.mapper.addMapping(self.txt_addresse_building, self.model.fieldIndex('addresseeHouseNo'))
        self.mapper.addMapping(self.txt_addresse_apt, self.model.fieldIndex('addresseeAptNo'))
        self.mapper.addMapping(self.txt_addresse_zip_code, self.model.fieldIndex('addresseeZipCode'))
        self.mapper.addMapping(self.fill_combo('tblPlaces', 'placeName', self.cbo_addresse_post_office),
                               self.model.fieldIndex('addresseePostOffice'))
        self.mapper.addMapping(self.fill_combo('tblPlaces', 'placeName', self.cbo_addresse_place),
                               self.model.fieldIndex('addresseeCity'))
        self.mapper.addMapping(self.txt_addresse_phone, self.model.fieldIndex('addresseePhone'))
        self.mapper.addMapping(self.txt_addresse_mobile, self.model.fieldIndex('addresseeCellPhone'))
        self.mapper.addMapping(self.txt_addresse_mail, self.model.fieldIndex('addresseeEmail'))

    def clear_all(self):
        self.deactivate_controls()
        self.txt_addresse_name.clear()
        self.cbo_addresse_street.clear()
        self.cbo_addresse_post_office.clear()
        self.txt_addresse_zip_code.clear()
        self.cbo_addresse_place.clear()
        self.txt_addresse_building.clear()
        self.txt_addresse_apt.clear()
        self.txt_addresse_phone.clear()
        self.txt_addresse_mobile.clear()
        self.txt_addresse_mail.clear()

    def on_search_clicked(self, checked):
        if checked:
            counter = 0
            if len(self.txt_search.text()) > 0:
                for item in range(self.model.rowCount()):
                    val = self.model.data(self.model.index(item, self.model.fieldIndex('addresseeName')))
                    if not val.__contains__(self.txt_search.text()):
                        self.lstvw_addressee.item(item).setHidden(True)
                        counter += 1
                if counter != self.lstvw_addressee.count():
                    for item in range(self.model.rowCount()):
                        if not self.lstvw_addressee.item(item).isHidden():
                            self.lstvw_addressee.setCurrentRow(item)
                            return
                else:
                    self.clear_all()
                    info_boxes.criticalBox("Brak adresata",
                                           "Nie odnaleziono adresata według podanego kryterium wyszukiwania")
                    self.btn_search.setChecked(False)
                    self.txt_search.clear()
                    self.set_listview_items()
                    self.lstvw_addressee.setFocus()
                    return
            else:
                info_boxes.criticalBox("Odmowa wykonania operacji",
                                       "Należy podać dane do wyszukania")
                self.btn_search.setChecked(False)
                self.lstvw_addressee.setFocus()
                return
        else:
            self.set_listview_items()
            self.txt_search.clear()
            self.lstvw_addressee.setFocus()

    def on_btn_add_clicked(self):
        self.activate_controls()
        row = int(self.model.rowCount())
        self.model.insertRow(row)
        if self.new_index is None:
            self.new_index = QModelIndex(self.model.index(row, 0))
        self.mapper.setCurrentModelIndex(self.new_index)
        self.lstvw_addressee.setCurrentIndex(self.new_index)
        self.lstvw_addressee.setCurrentRow(self.new_index.row())
        self.btn_edit.setEnabled(False)
        self.btn_remove.setEnabled(False)

    def on_btn_edit_clicked(self):
        self.activate_controls()
        self.btn_add.setEnabled(False)
        self.btn_remove.setEnabled(False)

    def on_btn_submit_clicked(self):
        if self.validate_form([self.txt_addresse_name, self.txt_addresse_building,
                               self.txt_addresse_zip_code, self.cbo_addresse_post_office,
                               self.cbo_addresse_place]):
            if self.new_index is not None:
                _row = self.new_index.row()
            else:
                _row = self.lstvw_addressee.currentRow()

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
            self.lstvw_addressee.setCurrentRow(0)
        self.deactivate_controls()
        self.txt_search.clear()
        self.btn_search.setChecked(False)
        self.lstvw_addressee.setFocus()

    def are_related_tables(self):
        row = self.lstvw_addressee.selectionModel().currentIndex().row()
        current = self.model.data(self.model.index(row, self.model.fieldIndex('addresseeName')))
        result = Query.are_related_records(self.db, 'tblLocalizations', 'ownerName', f'"{current}"')
        if result == 0:
            self.remove_data()
        else:
            info_boxes.criticalBox("Odmowa wykonania operacji",
                                   "Wybrana pozycja jest wykorzystana jako informacja w innej tabeli")
        self.lstvw_addressee.setFocus()

    def remove_data(self):
        if self.model.rowCount() > 0:
            row = self.lstvw_addressee.currentIndex().row()
            response = info_boxes.questionBox('Usunięcie danych',
                                              'Czy na pewno chcesz trwale usunąć bieżący wiersz ?')
            if response == 16384:
                self.model.removeRow(row)
                self.set_listview_items(row - 1)
        self.lstvw_addressee.setFocus()

    def show_addressbook(self, addressbook):
        self.clear_all()
        match addressbook:
            case 'servants':
                self.model.setTable("tblCollaborativeAddressee")
                self.lbl_addressee.setText('Dostawcy usług')
            case 'external':
                self.model.setTable("tblExternalsAddressee")
                self.lbl_addressee.setText('Adresaci zewnętrzni')
            case 'internal':
                self.model.setTable("tblInternalAddressee")
                self.lbl_addressee.setText('Adresaci wewnętrzni')

        self.model.select()
        self.set_listview_items()
        self.mapper.setModel(self.model)
        self.set_mapping()
        self.mapper.toFirst()
        if self.lstvw_addressee.count() == 0:
            self.btn_edit.setEnabled(False)
            self.btn_remove.setEnabled(False)
        self.show()

    def set_listview_items(self, row=0):
        self.lstvw_addressee.clear()
        self.model.sort(1, Qt.AscendingOrder)
        if self.model.rowCount() > 0:
            for item in range(self.model.rowCount()):
                val = self.model.data(self.model.index(item, self.model.fieldIndex('addresseeName')))
                self.lstvw_addressee.addItem(val)
        self.lstvw_addressee.setCurrentRow(row)

    def activate_controls(self):
        self.btn_ok.setEnabled(True)
        self.txt_addresse_name.setReadOnly(False)
        self.cbo_addresse_street.setEnabled(True)
        self.cbo_addresse_post_office.setEnabled(True)
        self.txt_addresse_zip_code.setReadOnly(False)
        self.cbo_addresse_place.setEnabled(True)
        self.txt_addresse_building.setReadOnly(False)
        self.txt_addresse_apt.setReadOnly(False)
        self.txt_addresse_phone.setReadOnly(False)
        self.txt_addresse_mobile.setReadOnly(False)
        self.txt_addresse_mail.setReadOnly(False)
        self.txt_addresse_name.setFocus()

    def deactivate_controls(self):
        self.btn_ok.setEnabled(False)
        self.txt_addresse_name.setReadOnly(True)
        self.cbo_addresse_street.setEnabled(False)
        self.cbo_addresse_post_office.setEnabled(False)
        self.txt_addresse_zip_code.setReadOnly(True)
        self.cbo_addresse_place.setEnabled(False)
        self.txt_addresse_building.setReadOnly(True)
        self.txt_addresse_apt.setReadOnly(True)
        self.txt_addresse_phone.setReadOnly(True)
        self.txt_addresse_mobile.setReadOnly(True)
        self.txt_addresse_mail.setReadOnly(True)
        self.lstvw_addressee.setFocus()

    def on_list_addressee_changed(self):
        if not self.btn_add.isEnabled():
            self.btn_add.setEnabled(True)
        if not self.btn_edit.isEnabled():
            self.btn_edit.setEnabled(True)
        if not self.btn_remove.isEnabled():
            self.btn_remove.setEnabled(True)
        row = self.lstvw_addressee.currentRow()
        if row is not None:
            self.mapper.setCurrentModelIndex(self.model.index(row, 0))
            self.deactivate_controls()

    def fill_combo(self, table, field, combo, command_type='select'):
        _list = Query.get_field_list(table, field, self.db, command_type)
        if not _list:
            pass
        else:
            new_list = []
            for item in _list:
                if item.find(',') == -1:
                    continue
                new_list.append(item[:item.index(',')])
            if len(new_list) > 0:
                new_list.sort()
                combo.addItems(new_list)
            else:
                _list.sort()
                combo.addItems(_list)
            combo.setCurrentIndex(-1)
        return combo

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