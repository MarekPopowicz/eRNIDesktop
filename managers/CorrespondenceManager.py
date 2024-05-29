from managers import TableManager


class CorrespondenceManager(TableManager.TableManager):
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase):
        super().__init__(table, db_table_name, column_titles, statusBar, dbase)

        self.set_model()

        self.change_filter('projectID = "{}"')
        self.setup_view()
        self.set_table_header_names()

        self.set_column_hidden(0)
        self.set_column_hidden(3)
        self.set_column_hidden(8)
        self.set_column_hidden(9)
        self.set_column_sort_desc(4)
        self.change_columns_order(7, 2)
        self.set_column_width(2, 250)
        self.set_column_width(5, 250)
        self.set_column_width(6, 250)

        self.table.clicked.connect(self.get_cell_value)