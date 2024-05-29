from PyQt5.QtWidgets import QDialog
from mappers import Mapper
from ui.device_mapper import Ui_Form


class DeviceMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, device_idx=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)
        Mapper.Mapper.__init__(self, manager, device_idx, controls)
        self.setupUi(self)

        self.add_mapping(self.dsbx_lenght, "deviceLenght")
        self.add_mapping(self.dsbx_width, "deviceWidth")
        self.add_mapping(self.cbo_voltage, "deviceVoltage")
        self.set_relation_field(["tblDeviceCategories", "deviceCategoryID", "deviceCategoryName"],
                                self.model.fieldIndex("deviceCategoryName"), self.cbo_device_name)
        self.fill_combo(self.manager.dbase, 'tblPSPelement', 'elementValue', self.cbo_PSPelement)
        self.add_mapping(self.cbo_PSPelement, "devicePSPelement")
        self.add_mapping(self.txt_Info, "deviceAdditionalInfo")

        self.cbo_voltage.addItems(['Niskie', 'Średnie', 'Wysokie'])
        self.cbo_voltage.setCurrentIndex(-1)

        self.dsbx_lenght.valueChanged.connect(lambda: self.current_area(self.dsbx_width.value(), self.dsbx_lenght.value()))
        self.dsbx_width.valueChanged.connect(lambda: self.current_area(self.dsbx_width.value(), self.dsbx_lenght.value()))
        self.btn_ok.clicked.connect(self.on_submit)
        self.current_area()

    def set_index(self, index):
        self.index = index
        idx = self.manager.parent.model.index(self.manager.parent.current_row(), 0)
        project_id = self.manager.parent.model.data(idx)
        self.set_header_info(self.lbl_projectId, self.lbl_task_name, project_id)
        self.set_localization_info()

        if self.index is not None:  # edit
            self.select_item()
            self.current_row = self.index.row()
            self.current_area(self.dsbx_width.value(), self.dsbx_lenght.value())
        else:  # add new
            self.current_row = self.add_new_row()
            self.current_area()
            self.clear_controls()
            self.bind_id()

    def bind_id(self):
        # set model data on current project id
        _id = self.manager.parent.model.data(
            self.manager.parent.model.index(self.manager.parent.current_row(), self.manager.parent.model.fieldIndex("projectID")))
        self.model.setData(self.model.index(self.current_row, self.model.fieldIndex("projectID")), _id)

        # set model on current localization id
        localization_id_index = self.model.fieldIndex("localizationID")
        self.model.setData(self.model.index(self.current_row, localization_id_index), self.manager.current_parent_row)

    def set_localization_info(self):
        values = []
        for item in range(self.manager.parent.localization_manager.model.columnCount()):
            idx = self.manager.parent.localization_manager.model.index(
                self.manager.parent.localization_manager.current_row(), item)
            values.append(self.manager.parent.localization_manager.model.data(idx))
        self.lbl_localization.setText(f'Dz. nr {values[3]}, AM-{round(values[2])}, Obręb {values[4]}')

    def current_area(self, width=0, length=0):
        result = round((width * length), 2)
        self.lbl_surface.setText(f"{result} m. kw.")

    def on_submit(self):
        if self.validate_form([self.dsbx_lenght, self.dsbx_width, self.cbo_voltage, self.cbo_device_name]):
            if self.mapper.submit():
                if not self.manager.parent.tabs_case_segments.isEnabled():
                    self.manager.parent.tabs_case_segments.setEnabled(True)

                self.close()
            else:
                self.model_last_error_msg()

    def clear_controls(self):
        self.cbo_device_name.setCurrentIndex(-1)
        self.cbo_voltage.setCurrentIndex(-1)