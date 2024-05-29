from controls import Controls
from mappers import RegulationMapper


class RegulationControl(Controls.Controls):
    def __init__(self, controls, table_manager):
        super().__init__(table_manager)
        self.btn_deed_add = controls[0]
        self.btn_deed_edit = controls[1]
        self.btn_deed_delete = controls[2]
        self.btn_deed_print = controls[3]
        self.action_deal = controls[4]

        self.mapper = RegulationMapper.RegulationMapper(self.manager, self)

        self.btn_deed_add.clicked.connect(self.add_deed_mapper)
        self.btn_deed_edit.clicked.connect(self.edit_deed_mapper)
        self.btn_deed_delete.clicked.connect(self.remove_regulation)
        self.btn_deed_print.clicked.connect(self.print_regulations)
        self.action_deal.triggered.connect(self.add_deed_mapper)

    def edit_deed_mapper(self):
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edit data
        self.mapper.show()
        self.enable_buttons(False)

    def add_deed_mapper(self):
        if self.manager.parent.model.rowCount() == 0:
            return
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(None)
        self.mapper.set_initial_data()
        self.mapper.clear_data()
        self.mapper.show()
        self.enable_buttons(False)

    def print_regulations(self):
        caption_text = f'<span style = "color: #c71b38;">({self.get_project_data("projectID")})</span> <span>{self.get_project_data("projectSapNo")}</span><span style = "padding: 10px 10px"> Umowy</span>'
        self.print('regulation_report', caption_text, self.get_project_data("projectID"))

    def remove_regulation(self):
        result = self.remove_row()
        if result is None or result == -1  or result == True:
            return

        else:  # no more rows - disable controls
            self.manager.parent.tabs_case_segments.setTabEnabled(5, False)

    def enable_buttons(self, bool_value):
        self.btn_deed_add.setEnabled(bool_value)
        self.btn_deed_edit.setEnabled(bool_value)
        self.btn_deed_delete.setEnabled(bool_value)
        self.action_deal.setEnabled(bool_value)
