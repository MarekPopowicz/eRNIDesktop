from managers import TableManager


class RegulationManager(TableManager.TableManager):
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase):
        super().__init__(table, db_table_name, column_titles, statusBar, dbase)

        self.set_model()
        self.set_relation(7, "tblRegulationCategories", "regulationCategoryID", "regulationCategoryName")
        self.change_filter('projectID = "{}"')
        self.setup_view()
        self.set_table_header_names()
        self.set_column_hidden(0)
        self.set_column_hidden(1)
        self.set_column_sort_desc(3)
        self.change_columns_order(5, 3)
        self.change_columns_order(6, 5)
        self.change_columns_order(5, 4)
        self.set_column_sort_desc(5)

        self.set_column_aligned(2)
        self.set_column_aligned(4)
        self.set_column_aligned(7)

        self.set_column_float_format(self.model.fieldIndex('regulationCost'))

        self.set_columns_fit_to_content()

        self.table.clicked.connect(self.get_cell_value)