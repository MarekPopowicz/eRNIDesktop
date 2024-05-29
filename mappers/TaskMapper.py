from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QDialog
import db.Query
from inspectors import SegmentInspector
from managers import ProjectManager
from mappers import LocalizationMapper
from mappers import Mapper
from ui.task_mapper import Ui_Dialog
from utils import file_io


class TaskMapper(QDialog, Ui_Dialog, Mapper.Mapper):
    def __init__(self, manager, controls, index=None):
        QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        Mapper.Mapper.__init__(self, manager, index, controls)
        self.setupUi(self)
        self.segment_inspector = None
        self.localization_mapper = None
        self.project_manager = None
        self.txt_project.installEventFilter(self)
        self.set_mapping()
        self.btn_ok.clicked.connect(self.on_submit)
        self.btn_check_segment.clicked.connect(self.check_segments)
        self.btn_project_manager.clicked.connect(self.on_project_manager)

    def on_project_manager(self):
        if self.project_manager is None:
            self.project_manager = ProjectManager.ProjectManager(self.manager.dbase, self)
        self.project_manager.show()

    def set_mapping(self):
        self.mapper.addMapping(self.txt_teczka, 0)
        self.mapper.addMapping(self.fill_combo(self.manager.dbase, 'tblProjects', 'projectSegment', self.cbo_segment, 'distinct'), 1)
        self.mapper.addMapping(self.txt_project, 2)
        self.cbo_priority.addItems(['Nie', 'Tak'])
        self.mapper.addMapping(self.cbo_priority, 3)

        self.set_relation_field(["tblStatus", "StatusId", "statusName"], self.model.fieldIndex("statusName"), self.cbo_status, 5)
        self.mapper.addMapping(self.fill_combo(self.manager.dbase, 'tblProjectTaskCategories', 'projectTaskName', self.cbo_task), 5)
        self.mapper.addMapping(self.fill_combo(self.manager.dbase, 'tblProjectManagers', 'projectManager', self.cbo_manager), 6)
        self.mapper.addMapping(self.dta_inflow, 7)
        self.dta_inflow.setDate(self.manager.current_date)

        self.set_relation_field(["tblProjectCategories", "projectCategoryID", "projectCategoryName"],
                                self.model.fieldIndex("projectCategoryName"), self.cbo_project_category)
        self.mapper.addMapping(self.txt_foreign_sign, 9)
        self.mapper.addMapping(self.dta_deadline, 10)
        self.dta_deadline.setDate(self.manager.current_date)
        self.mapper.addMapping(self.txt_additional_info, 12)
        self.mapper.addMapping(self.txt_link, 13)

    def closeEvent(self, event):
        if self.index is not None:
            self.manager.select_row(self.index.row())
        else:
            self.manager.select_model()
            self.manager.select_row()
        self.launch_controls.enable_buttons(True)
        self.manager.tabs_case_segments.setCurrentIndex(0)
        self.manager.table.setFocus()


    def on_submit(self):
        if self.validate_form([self.cbo_segment, self.cbo_task, self.cbo_manager, self.cbo_project_category, self.txt_project]):
            if self.mapper.submit():
                if self.manager.model.rowCount() > 0:
                    if not self.manager.button_next.isEnabled() and not self.manager.button_previous.isEnabled():
                        self.manager.set_controls(True)
                        self.manager.set_search_controls(True)

                    if not self.manager.task_controls[1].isEnabled() and not self.manager.task_controls[2].isEnabled():
                        self.manager.set_task_controls(True)
                self.close()

                self.create_work_folder()
                if self.index is not None:
                    self.manager.on_row_changed()
                    return
                self.manager.select_model()
                self.model.sort(0, Qt.DescendingOrder)
                self.manager.select_row()
                counter = self.manager.row_count()
                self.manager.info.setText('Ilość: ' + str(counter))

                self.localization_mapper = LocalizationMapper.LocalizationMapper(self.manager.localization_manager,
                                                                                 self.launch_controls.controls)  # add new localization

                self.localization_mapper.set_header_info(self.localization_mapper.lbl_projectId, self.localization_mapper.lbl_task_name)
                self.localization_mapper.set_index(None)
                self.localization_mapper.clear_controls()
                self.localization_mapper.show()
            else:
                self.model_last_error_msg()

    def check_segments(self):
        if self.segment_inspector is None:
            self.segment_inspector = SegmentInspector.SegmentInspector(self.manager.dbase, parent=self)
        else:
            self.segment_inspector.set_position()
            self.segment_inspector.load_content()
        self.segment_inspector.lstvw_segments.setCurrentIndex(self.segment_inspector.lstvw_segments.model().index(0, 0))
        self.segment_inspector.show()

    def keyPressEvent(self, qKeyEvent):
        # print(qKeyEvent.key())
        if qKeyEvent.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.on_submit()
        else:
            super().keyPressEvent(qKeyEvent)

    def eventFilter(self, source, event):
        if event.type() == QEvent.FocusIn:
            if source is self.txt_project:
                if len(self.txt_project.text()) == 0:
                    self.txt_project.setText('I-WR-')
        return super(TaskMapper, self).eventFilter(source, event)

    def clear_controls(self):

        if self.index is not None:
            self.select_item()
        else:
            self.add_new_row()
            _id = db.Query.get_max_id_value(self.manager.dbase, self.manager.table_name, 'projectID')
            if _id == '':
                _id = 0
            self.txt_teczka.setText(str(_id + 1))
            row = self.manager.model.rowCount()
            idx = self.manager.model.index(row - 1, 0)
            self.manager.model.setData(idx, str(_id + 1))

        self.cbo_priority.setCurrentIndex(0)
        self.cbo_status.setCurrentIndex(5)
        self.cbo_task.setCurrentIndex(-1)

        self.cbo_segment.clear()
        self.fill_combo(self.manager.dbase, 'tblProjects', 'projectSegment', self.cbo_segment, 'distinct')
        self.cbo_segment.setCurrentIndex(-1)
        self.cbo_manager.clear()
        self.fill_combo(self.manager.dbase, 'tblProjectManagers', 'projectManager', self.cbo_manager)
        self.cbo_task.clear()
        self.fill_combo(self.manager.dbase, 'tblProjectTaskCategories', 'projectTaskName', self.cbo_task)
        self.cbo_manager.setCurrentIndex(-1)
        self.dta_inflow.setDate(self.manager.current_date)
        self.cbo_project_category.setCurrentIndex(-1)
        self.dta_deadline.setDate(self.manager.current_date)

    def create_work_folder(self):
        settings = file_io.read_encoded('config.txt')
        path = settings[2] + '\\' + str(self.txt_teczka.text())
        file_io.create_folder(path)