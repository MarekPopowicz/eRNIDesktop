import db.Query
from mappers import LocalizationMapper
from utils import info_boxes


class LocalizationControl:
    def __init__(self, controls, table_manager):
        self.btn_localization_add = controls[0]
        self.btn_localization_edit = controls[1]
        self.btn_localization_delete = controls[2]
        self.action_localization = controls[3]
        self.device_controls = controls[4]
        self.manager = table_manager
        self.mapper = None

        self.btn_localization_edit.clicked.connect(self.edit_localization_mapper)
        self.btn_localization_add.clicked.connect(self.add_localization_mapper)
        self.btn_localization_delete.clicked.connect(self.remove_localization)
        self.action_localization.triggered.connect(self.add_localization_mapper)

    def edit_localization_mapper(self):
        self.mapper = LocalizationMapper.LocalizationMapper(self.manager, self)
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edit data
        place = self.manager.model.data(self.manager.model.index(self.manager.table.currentIndex().row(), 8))
        index = self.mapper.cbo_place.findText(place)
        self.mapper.cbo_place.setCurrentIndex(index)
        self.mapper.show()
        self.enable_buttons(False)

    def add_localization_mapper(self):
        if self.manager.parent.model.rowCount() == 0:
            return
        self.mapper = LocalizationMapper.LocalizationMapper(self.manager, self)
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(None) # set current table index to add data
        self.mapper.clear_controls()
        self.mapper.show()
        self.enable_buttons(False)

    def remove_localization(self):
        if self.manager.model.rowCount() > 0:
            idx = self.manager.model.index(self.manager.current_row(), 0)
            localization_id = self.manager.model.data(idx)
            response = info_boxes.questionBox('Usunięcie danych',
                                              'Czy chcesz trwale usunąć wybraną lokalizację ?\n\n'
                                                    'Usunięcie lokalizacji usunie także wszystkie\npowiązane z nią urządzenia.')
            if response == 16384:
                db.Query.delete_records(self.manager.dbase, 'tblDevices', 'localizationID', localization_id) # delete from device table
                self.manager.device_manager.select_model() # refresh device view
                self.manager.model.removeRow(self.manager.table.currentIndex().row()) # delete localization record
                self.manager.select_model() # refresh localization view
                if self.manager.model.rowCount() > 0: # is there any row else ?
                    self.manager.table.selectRow(0)
                else:
                    self.manager.parent.tabs_case_segments.setTabEnabled(0, False) # if not disable localization tab
                    self.manager.parent.table.setFocus()

    def enable_buttons(self, bool_value):
        self.btn_localization_add.setEnabled(bool_value)
        self.btn_localization_edit.setEnabled(bool_value)
        self.btn_localization_delete.setEnabled(bool_value)
        self.action_localization.setEnabled(bool_value)
