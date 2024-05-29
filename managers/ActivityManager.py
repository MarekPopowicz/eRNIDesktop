from managers import TableManager
from PyQt5.QtWidgets import QApplication


class ActivityManager(TableManager.TableManager):
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase):
        super().__init__(table, db_table_name, column_titles, statusBar, dbase)

        self.set_model()

        self.task_details_manager = None
        self.change_filter('projectID = "{}"')
        self.setup_view()
        self.set_table_header_names()

        self.set_column_hidden(0)
        self.set_column_hidden(3)
        self.set_column_hidden(4)
        self.set_column_sort_desc(1)

        self.set_columns_fit_to_content()
        # self.set_rows_fit_to_content()

        self.table.clicked.connect(self.get_cell_value)

    def get_cell_value(self, index):
        clipboard = QApplication.clipboard()
        for item in range(len(self.column_titles)):
            if item == index.column():
                cell_value = index.data()
                if len(str(cell_value)) > 0:
                    clipboard.setText(str(cell_value))
                return True