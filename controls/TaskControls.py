import db.Query
from mappers import TaskMapper
from controls import Controls
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from utils import info_boxes


class TaskControl(Controls.Controls):
    def __init__(self, table_manager, controls):
        super().__init__(table_manager)

        self.btn_task_add = table_manager.task_controls[0]
        self.btn_task_edit = table_manager.task_controls[1]
        self.btn_task_delete = table_manager.task_controls[2]
        self.btn_task_print = table_manager.task_controls[3]
        self.btn_task_clipboard = table_manager.task_controls[4]
        self.action_task = table_manager.task_controls[5]
        self.controls = controls  # localization_controls, device_controls

        self.mapper = TaskMapper.TaskMapper(self.manager, self)

        self.btn_task_print.clicked.connect(self.on_btn_print_clicked)
        self.btn_task_edit.clicked.connect(self.edit_task_mapper)
        self.btn_task_add.clicked.connect(self.add_task_mapper)
        self.btn_task_delete.clicked.connect(self.remove_row)
        self.action_task.triggered.connect(self.add_task_mapper)
        self.btn_task_clipboard.clicked.connect(self.on_btn_task_clipboard_clicked)

        if table_manager.model.rowCount() == 0:
            self.btn_task_add.setEnabled(True)
            self.btn_task_edit.setEnabled(False)
            self.btn_task_delete.setEnabled(False)
            self.btn_task_print.setEnabled(False)
            self.btn_task_clipboard.setEnabled(False)

    def edit_task_mapper(self):
        self.mapper.cbo_manager.clear()
        self.mapper.fill_combo(self.manager.dbase, 'tblProjectManagers', 'projectManager', self.mapper.cbo_manager)
        self.mapper.cbo_task.clear()
        self.mapper.fill_combo(self.manager.dbase, 'tblProjectTaskCategories', 'projectTaskName', self.mapper.cbo_task)
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edit data
        self.mapper.show()
        self.enable_buttons(False)

    def add_task_mapper(self):
        self.mapper.set_index(None)
        self.mapper.clear_controls()
        self.mapper.show()
        self.enable_buttons(False)

    def on_btn_print_clicked(self):
        filter_description = 'Zadania'
        if self.manager.btn_search.isChecked():
            filter_description = f'{self.manager.cbo_search_table.currentText()} &#8594; ' \
                                 f'{self.manager.cbo_search_column.currentText()} ' \
                                 f'{self.manager.cbo_search_sql_operators.currentText()} "{self.manager.txt_search_value.text()}"'

        caption_text = f'<span>({self.manager.info.text()})</span> <span>{filter_description}</span>'
        self.print('tasks_report', caption_text)

    def on_btn_task_clipboard_clicked(self):
        row_data = {}
        row = self.manager.table.currentIndex().row()
        for item in range(len(self.manager.column_titles)):
            idx = self.manager.model.index(row, item)
            value = self.manager.model.data(idx)
            header = self.manager.model.headerData(item, Qt.Horizontal, Qt.DisplayRole)
            if value == '':
                row_data[header] = '-'
            else:
                row_data[header] = value
        clipboard = QApplication.clipboard()
        text = ''
        for item in row_data.items():
            text += f'{item[0]}: {item[1]} \n'
        clipboard.setText(text)

    def remove_row(self):
        response = info_boxes.questionBox('Usunięcie danych',
                                          'Czy na pewno chcesz trwale usunąć bieżący wiersz ?\n\n'
                                          'Usunięcie zdania usunie także wszystkie\npowiązane z nim informacje.')
        if response == 16384:
            db.Query.delete_records(self.manager.dbase, 'tblDevices', 'projectID',
                                    self.manager.current_parent_row)  # delete from devices table
            db.Query.delete_records(self.manager.dbase, 'tblLocalizations', 'projectID',
                                    self.manager.current_parent_row)  # delete from localization table
            db.Query.delete_records(self.manager.dbase, 'tblActions', 'projectID',
                                    self.manager.current_parent_row)  # delete from actions table
            db.Query.delete_records(self.manager.dbase, 'tblInvoices', 'projectID',
                                    self.manager.current_parent_row)  # delete from invoices table
            db.Query.delete_records(self.manager.dbase, 'tblKeyDocuments', 'projectID',
                                    self.manager.current_parent_row)  # delete from documents table
            db.Query.delete_records(self.manager.dbase, 'tblProjectCorrespondence', 'projectID',
                                    self.manager.current_parent_row)  # delete from correspondence table
            db.Query.delete_records(self.manager.dbase, 'tblPropertyDocuments', 'projectID',
                                    self.manager.current_parent_row)  # delete from property documents table
            db.Query.delete_records(self.manager.dbase, 'tblRegulations', 'projectID',
                                    self.manager.current_parent_row)  # delete from regulations table

            self.manager.model.removeRow(self.manager.table.currentIndex().row())

            # refresh table data
            self.manager.select_model()
            self.manager.localization_manager.select_model()
            self.manager.localization_manager.device_manager.select_model()
            self.manager.document_manager.select_model()
            self.manager.correspondence_manager.select_model()
            self.manager.activity_manager.select_model()
            self.manager.invoice_manager.select_model()
            self.manager.regulation_manager.select_model()
            self.manager.property_document_manager.select_model()

            if self.manager.model.rowCount() == 0:
                self.manager.disable_controls()
                self.manager.set_task_controls(False)
                self.manager.task_details.taskDetails.clear()
                self.manager.task_details.taskInfo.clear()
                return
            self.manager.info.setText('Ilość: ' + str(self.manager.row_count()))
            self.manager.table.selectRow(0)


    def enable_buttons(self, bool_value):
        self.btn_task_add.setEnabled(bool_value)
        self.btn_task_edit.setEnabled(bool_value)
        self.btn_task_delete.setEnabled(bool_value)