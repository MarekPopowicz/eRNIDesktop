from PyQt5.QtWidgets import QDialog
from mappers import Mapper
from ui.asset_mapper import Ui_Form


class PropertyDocumentMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, index=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)
        Mapper.Mapper.__init__(self, manager, index, controls)
        self.setupUi(self)

        self.btn_ok.clicked.connect(self.on_submit)
        self.set_mapping()

    def on_submit(self):
        if self.validate_form(
                [self.cbo_type, self.txt_SAP]
        ):
            if self.mapper.submit():
                if not self.manager.parent.tabs_case_segments.isTabEnabled(6):
                    self.manager.parent.tabs_case_segments.setTabEnabled(6, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(6)
                self.close()
            else:
                self.model_last_error_msg()

    def set_mapping(self):

        self.cbo_type.addItems(['OT', 'PT'])
        self.add_mapping(self.cbo_type, "propertyDocumentType")
        self.add_mapping(self.dta_date, "propertyDocumentSapRegistrationDate")
        self.add_mapping(self.txt_SAP, "propertyDocumentSapRegisterNo")
        self.add_mapping(self.txt_info, "propertyDocumentAdditionalInfo")

    def clear_data(self):
        self.cbo_type.setCurrentIndex(0)
        self.dta_date.setDate(self.manager.current_date)