from managers import TableManager


class DeviceManager(TableManager.TableManager):
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase):
        super().__init__(table, db_table_name, column_titles, statusBar, dbase)

        self.set_model()
        self.set_relation(4, "tblDeviceCategories", "deviceCategoryID", "deviceCategoryName")
        self.change_filter('localizationID = "{}"')
        self.parent = None
        self.setup_view()
        self.set_table_header_names()
        self.set_column_aligned(1)
        self.set_column_aligned(2)
        self.change_columns_order(6, 7)
        self.set_column_hidden(0)
        self.set_column_hidden(5)
        self.set_column_hidden(8)
        self.set_column_fit_to_content(1)
        self.set_column_fit_to_content(2)
        self.set_column_fit_to_content(7)
        self.set_column_float_format(self.model.fieldIndex('deviceLenght'))
        self.set_column_float_format(self.model.fieldIndex('deviceWidth'))
        self.table.clicked.connect(self.get_cell_value)