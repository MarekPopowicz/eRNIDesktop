from managers import TableManager
from utils import restoration


class LocalizationManager(TableManager.TableManager):
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase, device_manager):
        super().__init__(table, db_table_name, column_titles, statusBar, dbase)
        self.restorationAgent = restoration.RestorationAgent()
        self.device_manager = device_manager
        self.device_manager.parent = self
        self.column_values = {}
        self.column_titles = column_titles

        self.set_model()
        self.set_relation(7, "tblRegions", "regionId", "regionName")
        self.set_relation(5, "tblStatus", "StatusId", "statusName")
        self.set_relation(8, "tblPlaces", "placeID", "placeName")
        self.change_filter('projectID = "{}"')

        self.setup_view()
        self.set_table_header_names()
        self.set_column_hidden(0)
        self.set_column_hidden(9)
        self.set_column_aligned(2)
        self.set_column_aligned(3)
        self.set_column_fit_to_content(1)
        self.set_column_fit_to_content(2)
        self.set_column_fit_to_content(3)
        self.set_column_stretched(10)
        self.change_columns_order(12, 10)

        self.table.selectionModel().selectionChanged.connect(self.on_row_changed)
        self.table.clicked.connect(self.get_cell_value)

    def on_row_changed(self):
        val = self.model.data(self.model.index(self.current_row(), 0))
        self.device_manager.current_parent_row = int(val)
        self.device_manager.change_filter('localizationID = "{}"')

    def on_row_absence(self):
        self.device_manager.current_parent_row = -1
        self.device_manager.change_filter('localizationID = "{}"')
        # self.device_manager.model.select()