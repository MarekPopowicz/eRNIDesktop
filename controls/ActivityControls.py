from PyQt5.QtCore import QDate
from controls import Controls
from mappers import ActivityMapper


class ActivityControl(Controls.Controls):
    def __init__(self, controls, table_manager):
        super().__init__(table_manager)
        self.btn_activity_add = controls[0]
        self.btn_activity_edit = controls[1]
        self.btn_activity_delete = controls[2]
        self.btn_activity_print = controls[3]
        self.actionCzynno = controls[4]

        self.mapper = ActivityMapper.ActivityMapper(self.manager, self)

        self.btn_activity_edit.clicked.connect(self.edit_activity_mapper)
        self.btn_activity_add.clicked.connect(self.add_activity_mapper)
        self.btn_activity_delete.clicked.connect(self.remove_activity)
        self.btn_activity_print.clicked.connect(self.print_activities)
        self.actionCzynno.triggered.connect(self.add_activity_mapper)

    def edit_activity_mapper(self):
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edit data
        self.mapper.show()
        self.enable_buttons(False)
        self.mapper.txt_activity_description.setFocus()

    def add_activity_mapper(self):
        if self.manager.parent.model.rowCount() == 0:
            return
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(None)
        self.mapper.dta_activity_date.setDate(QDate.currentDate())
        self.mapper.show()
        self.enable_buttons(False)
        self.mapper.txt_activity_description.setFocus()

    def print_activities(self):
        caption_text = f'<span style = "color: #c71b38;">({self.get_project_data("projectID")})</span> <span>{self.get_project_data("projectSapNo")}</span><span style = "padding: 10px 10px"> Czynności</span>'
        self.print('activities_report', caption_text, self.get_project_data("projectID"))

    def remove_activity(self):
        result = self.remove_row()
        if result is None or result == -1 or result == True:
            return

        else:  # no more rows - disable controls
            self.manager.parent.tabs_case_segments.setTabEnabled(3, False)

    def enable_buttons(self, bool_value):
        self.btn_activity_add.setEnabled(bool_value)
        self.btn_activity_edit.setEnabled(bool_value)
        self.btn_activity_delete.setEnabled(bool_value)
        self.actionCzynno.setEnabled(bool_value)