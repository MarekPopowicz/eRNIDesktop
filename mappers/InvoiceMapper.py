from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QDialog
from inspectors import AddresseeInspector
from managers import AddressBookManager
from mappers import Mapper
from ui.invoice_mapper import Ui_Form
from utils import info_boxes


class InvoiceMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, index=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)
        Mapper.Mapper.__init__(self, manager, index, controls)
        self.setupUi(self)

        self.addressbook = None
        self.btn_ok.clicked.connect(self.on_submit)
        self.btn_addressbook.clicked.connect(self.addressbook_open)
        self.btn_addressee_inspector.clicked.connect(self.addressee_inspector_open)
        self.btn_restore.clicked.connect(self.on_restore)
        self.addressee_inspector = None
        self.set_mapping()

    def on_submit(self):
        if self.validate_form([self.txt_number, self.txt_name, self.cbo_title, self.dta_registration_date, self.txt_SAP, self.dsb_netto,
                               self.sb_tax_value]):

            if self.dta_issue_date.date() == self.manager.current_date:
                response = info_boxes.questionBox('Uwaga',
                                                  'Data wydania dokumentu wskazuje na dzień dzisiejszy.\n Czy jest to poprawna informacja ?')
                if response != 16384:
                    return

            if self.mapper.submit():
                self.results.clear()
                self.btn_restore.setEnabled(False)
                if not self.manager.parent.tabs_case_segments.isTabEnabled(4):
                    self.manager.parent.tabs_case_segments.setTabEnabled(4, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(4)
                self.close()
            else:
                self.model_last_error_msg()
                self.catch_data()
                self.btn_restore.setEnabled(True)
                self.close()

    def catch_data(self):
        self.results.clear()
        self.results.append(self.dta_issue_date.date().toString())
        self.results.append(self.txt_number.text())
        self.results.append(self.txt_name.toPlainText())
        self.results.append(self.cbo_title.currentText())
        self.results.append(self.dsb_netto.value())
        self.results.append(self.sb_tax_value.value())
        self.results.append(self.dta_registration_date.date().toString())
        self.results.append(self.txt_SAP.text())
        self.results.append(self.txt_info.toPlainText())


    def on_restore(self):
        self.dta_issue_date.setDate(QDate.fromString(self.results[0]))
        self.txt_number.setText(self.results[1])
        self.txt_name.setPlainText(self.results[2])
        self.cbo_title.setCurrentText(self.results[3])
        self.dsb_netto.setValue(self.results[4])
        self.sb_tax_value.setValue(self.results[5])
        self.dta_registration_date.setDate(QDate.fromString(self.results[6]))
        self.txt_SAP.setText(self.results[7])
        self.txt_info.setPlainText(self.results[8])

    def set_mapping(self):
        self.add_mapping(self.dta_issue_date, "invoiceIssueDate")
        self.add_mapping(self.txt_number, "invoiceNo")
        self.add_mapping(self.txt_name, "invoiceSellerName")
        self.add_mapping(self.cbo_title, "invoiceTitle")
        self.fill_combo(self.manager.dbase, 'tblInvoiceCategories', 'invoiceTitle', self.cbo_title)
        self.add_mapping(self.dsb_netto, "invoiceNettoValue")
        self.add_mapping(self.sb_tax_value, "invoiceTax")
        self.add_mapping(self.dta_registration_date, "invoiceSapRegistrationDate")
        self.add_mapping(self.txt_SAP, "invoiceSapRegisterNo")
        self.add_mapping(self.txt_info, "invoiceAdditionalInfo")

    def set_date(self):
        self.dta_issue_date.setDate(self.manager.current_date)
        self.dta_registration_date.setDate(self.manager.current_date)

    def addressee_inspector_open(self):
        if self.addressee_inspector is None:
            self.addressee_inspector = AddresseeInspector.AddresseeInspector(self.manager.dbase, parent=self)
            self.addressee_inspector.setWindowTitle("Usługodawcy")
        self.addressee_inspector.set_position()
        table = 'tblCollaborativeAddressee'
        self.addressee_inspector.load_data(table)
        self.btn_addressee_inspector.hide()
        self.addressee_inspector.show()

    def addressbook_open(self):
        if self.addressbook is None:
            self.addressbook = AddressBookManager.AddresseeManager(self.manager.dbase, None)
        self.addressbook.show_addressbook('servants')

    def clear_data(self):
        self.cbo_title.setCurrentIndex(-1)
        self.dsb_netto.setValue(0)
        self.sb_tax_value.setValue(23)