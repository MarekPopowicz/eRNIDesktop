from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from db import Query
from inspectors import ActionInspector
from mappers import Mapper
from ui.activity_mapper import Ui_Form


class ActivityMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, index=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)
        Mapper.Mapper.__init__(self, manager, index, controls)
        self.setupUi(self)

        self.activity_inspector = None
        self.set_mapping()

        self.btn_activity_inspector.clicked.connect(self.activity_inspector_open)
        self.btn_ok.clicked.connect(self.on_submit)

    def activity_inspector_open(self):
        if self.activity_inspector is None:
            self.activity_inspector = ActionInspector.ActionInspector(self.manager.dbase, parent=self)
        self.activity_inspector.set_position()
        self.activity_inspector.show()

    def on_submit(self):
        if self.validate_form([self.txt_activity_description]):
            if self.mapper.submit():

                current_date = self.dta_activity_date.date().toString(Qt.ISODate)
                row = self.manager.parent.current_row()
                _id = self.manager.parent.current_parent_row
                if Query.update_value(self.manager.dbase, 'tblProjects', 'projectLastActivity', current_date, 'projectID', _id):
                    self.manager.parent.model.setData(
                        self.manager.parent.model.index(row, self.manager.parent.model.fieldIndex('projectLastActivity')), current_date)
                    if not self.manager.task_details_manager is None:
                        self.manager.task_details_manager.column_values['Aktywność'] = current_date
                        self.manager.task_details_manager.display_task_details()

                if not self.manager.parent.tabs_case_segments.isTabEnabled(3):
                    self.manager.parent.tabs_case_segments.setTabEnabled(3, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(3)
                self.close()
            else:
                self.model_last_error_msg()

    def set_mapping(self):
        self.dta_activity_date.setDate(self.manager.current_date)
        self.add_mapping(self.txt_activity_description, "actionDescription")
        self.add_mapping(self.dta_activity_date, "actionDate")
        self.add_mapping(self.cbx_keep_attention, "actionKeepAttention")