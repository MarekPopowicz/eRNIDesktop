from controls import Controls
from mappers import DeviceMapper


class DeviceControl(Controls.Controls):
    def __init__(self, controls, table_manager):
        super().__init__(table_manager)
        self.btn_device_add = controls[0]
        self.btn_device_edit = controls[1]
        self.btn_device_delete = controls[2]

        self.mapper = DeviceMapper.DeviceMapper(self.manager, self)

        self.btn_device_edit.clicked.connect(self.edit_device_mapper)
        self.btn_device_add.clicked.connect(self.add_device_mapper)
        self.btn_device_delete.clicked.connect(self.remove_device)


    def edit_device_mapper(self):
        if self.manager.model.rowCount() == 0:
            return
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edit data
        self.mapper.show()
        self.enable_buttons(False)

    def add_device_mapper(self):
        if self.manager.parent.localization_manager.model.rowCount() == 0: # no localization -> no devices
            return
        self.mapper.set_index(None)
        self.mapper.show()
        self.enable_buttons(False)

    def remove_device(self):
        result = self.remove_row()
        if result == -1 or result == True:
            return

    def enable_buttons(self, bool_value):
        self.btn_device_add.setEnabled(bool_value)
        self.btn_device_edit.setEnabled(bool_value)
        self.btn_device_delete.setEnabled(bool_value)
