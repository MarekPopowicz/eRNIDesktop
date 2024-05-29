from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from inspectors import AddresseeInspector
from managers import AddressBookManager
from mappers import Mapper
from ui.deal_mapper import Ui_Form
from utils import info_boxes


class RegulationMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, index=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)
        Mapper.Mapper.__init__(self, manager, index, controls)
        self.setupUi(self)

        self.addressbook = None
        self.btn_ok.clicked.connect(self.on_submit)
        self.btn_addressbook.clicked.connect(self.addressbook_open)
        self.btn_addressee_inspector.clicked.connect(self.addressee_inspector_open)
        self.cbo_type.currentTextChanged.connect(self.on_change_type)
        self.addressee_inspector = None
        self.set_mapping()
        self.localization_str = ''
        self.txt_number.textChanged.connect(self.set_file_description)
        self.dta_deal_date.dateChanged.connect(self.set_file_description)
        self.cbo_regulation.currentTextChanged.connect(self.set_file_description)

    def on_submit(self):
        if self.validate_form(
                [self.cbo_element, self.txt_name, self.cbo_type, self.txt_number, self.cbo_regulation]
        ):
            if self.mapper.submit():

                if self.dta_deal_date.date() == self.manager.current_date:
                    response = info_boxes.questionBox('Uwaga',
                                                      'Data dokumentu wskazuje na dzień dzisiejszy.\n Czy jest to poprawna informacja ?')
                    if response != 16384:
                        return

                if not self.manager.parent.tabs_case_segments.isTabEnabled(5):
                    self.manager.parent.tabs_case_segments.setTabEnabled(5, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(5)
                self.close()
            else:
                self.model_last_error_msg()

    def set_mapping(self):
        self.mapper.addMapping(
            self.fill_combo(self.manager.dbase, 'tblPSPelement', 'elementValue', self.cbo_element),
            self.model.fieldIndex("regulationSapElement"))

        self.add_mapping(self.txt_name, "regulationDocumentSource")
        self.cbo_type.addItems(['Akt notarialny', 'Zwykła forma pisemna', 'Decyzja administracyjna', 'Orzeczenie sądu'])
        self.add_mapping(self.cbo_type, "regulationDocumentType")
        self.add_mapping(self.dta_deal_date, "regulationDocumentDate")
        self.add_mapping(self.txt_number, "regulationDocumentSignature")
        self.set_relation_field(["tblRegulationCategories", "regulationCategoryID", "regulationCategoryName"],
                                self.model.fieldIndex("regulationCategoryName"),
                                self.cbo_regulation, 0)
        self.add_mapping(self.dsb_cost, "regulationCost")
        self.add_mapping(self.txt_file_description, "regulationDocumentLink")
        self.add_mapping(self.txt_info, "additionalInformation")

    def set_initial_data(self):
        self.dta_deal_date.setDate(self.manager.current_date)
        self.txt_number.setText('Rep. A. ')
        rows = self.manager.parent.localization_manager.model.rowCount()
        if rows == 0:
            info_boxes.warningBox('Opis dokumentu',
                                  'Brak danych o lokalizacji urządzeń uniemożliwia automatyczny opis dokumentu w polu \'Oznaczenie\'.')
            return
        localization_data = self.get_localization_data(rows)
        self.localization_str = self.set_localization_data(localization_data)
        self.set_file_description()

    def addressee_inspector_open(self):
        if self.addressee_inspector is None:
            self.addressee_inspector = AddresseeInspector.AddresseeInspector(self.manager.dbase, parent=self)
            self.addressee_inspector.setWindowTitle("Usługodawcy")
        table = 'tblCollaborativeAddressee'
        self.addressee_inspector.set_position()
        self.addressee_inspector.load_data(table)
        self.btn_addressee_inspector.hide()
        self.addressee_inspector.show()

    def addressbook_open(self):
        if self.addressbook is None:
            self.addressbook = AddressBookManager.AddresseeManager(self.manager.dbase, None)
        self.addressbook.show_addressbook('servants')

    def clear_data(self):
        self.cbo_element.setCurrentIndex(-1)
        self.dsb_cost.setValue(0)
        self.cbo_type.setCurrentIndex(0)
        self.txt_file_description.clear()
        self.cbo_regulation.setCurrentIndex(-1)
        self.txt_info.clear()
        self.txt_number.setText('Rep. A. ')

    def on_change_type(self, txt):
        if txt == 'Akt notarialny':
            self.txt_number.setText('Rep. A. ')
        else:
            self.txt_number.clear()

    def set_file_description(self):
        if not self.get_relevant_data():
            return
        localization_str = self.get_relevant_data().strip()
        txt = f'{self.dta_deal_date.date().toString(Qt.ISODate)} {self.txt_number.text()} {self.lbl_projectId.text()} {self.cbo_regulation.currentText()} {localization_str}.pdf'
        self.txt_file_description.setPlainText(txt.replace('/', '_'))

    def get_relevant_data(self):
        result = []
        if not self.localization_str:
            return False
        positions = self.localization_str.split('dz.')
        for i in range(1, len(positions)):
            result.append('dz. nr ' + (positions[i].split('gm.')[0].replace(';', '')))
        return ",".join(result).replace(',', '')