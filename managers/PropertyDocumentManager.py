from managers import TableManager


class PropertyDocumentManager(TableManager.TableManager):
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase):
        super().__init__(table, db_table_name, column_titles, statusBar, dbase)

        self.set_model()
        self.change_filter('projectID = "{}"')
        self.setup_view()
        self.set_table_header_names()
        self.set_column_hidden(0)
        self.set_column_hidden(5)
        self.set_column_sort_desc(3)
        self.change_columns_order(4, 1)
        self.change_columns_order(4, 2)
        self.change_columns_order(4, 3)

        self.set_columns_fit_to_content()

        self.table.clicked.connect(self.get_cell_value)