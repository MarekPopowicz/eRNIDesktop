from PyQt5 import QtCore, QtWidgets
from utils import delegates, styles
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel
from PyQt5.QtWidgets import QAbstractScrollArea, QHeaderView, QApplication
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
import webbrowser


class TableManager:
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase):
        self.table = table
        self.parent = None
        self.table_name = db_table_name
        self.column_titles = column_titles
        self.statusBar = statusBar
        self.dbase = dbase
        self.model = QSqlRelationalTableModel(db=self.dbase)

        self.current_date = QDate.currentDate()
        self.header = self.table.horizontalHeader()
        self.align_delegate = delegates.AlignDelegate(self.table)
        self.float_delegate = delegates.FloatDelegate(self.table)
        self.current_parent_row = 0
        super().__init__()

    def set_column_float_format(self, column_index):
        self.table.setItemDelegateForColumn(column_index, self.float_delegate)

    def set_model(self):
        self.model.setTable(self.table_name)

    def set_column_sort_desc(self, column_index):
        self.model.setSort(column_index, Qt.DescendingOrder)

    def set_relation(self, column_index, table, fk_id, col_name):
        self.model.setRelation(column_index, QSqlRelation(table, fk_id, col_name))

    def select_model(self):
        self.model.select()
        while self.model.canFetchMore():
            self.model.fetchMore()

    def setup_view(self):
        self.table.setModel(self.model)
        self.header.setSectionResizeMode(QHeaderView.Interactive)
        self.header.setDefaultAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setFont(QFont("Tahoma", 10))
        self.header.setFont(QFont("Tahoma", 10))
        self.table.setStyleSheet(styles.QHeaderView_qss)

    def set_table_header_names(self):
        for n, t in self.column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Horizontal, t)

    def set_column_fit_to_content(self, column_index):
        self.header.setSectionResizeMode(column_index, QtWidgets.QHeaderView.ResizeToContents)

    def set_column_stretched(self, column_index):
        self.header.setSectionResizeMode(column_index, QtWidgets.QHeaderView.Stretch)

    def set_column_width(self, column, width):
        self.table.setColumnWidth(column, width)

    def set_column_aligned(self, column_index):
        self.table.setItemDelegateForColumn(column_index, self.align_delegate)

    def set_column_hidden(self, column_index):
        self.table.setColumnHidden(column_index, True)

    def set_columns_min_width(self, width):
        self.header.setMinimumSectionSize(width)

    def set_rows_fit_to_content(self):
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def set_columns_fit_to_content(self):
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def change_columns_order(self, pos_from, pos_to):
        self.table.horizontalHeader().moveSection(pos_from, pos_to)

    def change_filter(self, str_filter):

        # use str_filter like: 'projectID = "{}"'
        while self.model.canFetchMore():
            self.model.fetchMore()
        filter_str = str_filter.format(self.current_parent_row)
        self.model.setFilter(filter_str)
        self.model.select()
        row_count = self.model.rowCount()
        # print(self.table.objectName(), row_count)
        if row_count > 0:
            self.table.selectRow(0)
            return True
        else:
            return False

    def select_row(self, index=0):
        if self.model.rowCount() > 0:
            self.table.selectRow(index)
            self.table.scrollTo(self.table.currentIndex())

    def row_count(self):
        while self.model.canFetchMore():
            self.model.fetchMore()
        return self.model.rowCount()

    def current_row(self):
        row = 0
        index = self.table.selectionModel().selectedRows()
        for index in sorted(index):
            row = index.row()
        return row

    def get_cell_value(self, index):
        clipboard = QApplication.clipboard()
        for item in range(len(self.column_titles)):
            if item == index.column():
                header = self.model.headerData(item, Qt.Horizontal, Qt.DisplayRole)
                cell_value = index.data()
                if len(str(cell_value)) > 0:
                    if header == "Link":
                        webbrowser.open(cell_value)
                        return
                    msg = f'{header} : {cell_value}'
                    clipboard.setText(str(cell_value))
                    self.statusBar.showMessage(msg)
                else:
                    self.statusBar.clearMessage()
                return True

    def on_row_changed(self):
        for item in range(len(self.column_titles)):
            idx = self.model.index(self.current_row(), item)
            value = self.model.data(idx)
            header = self.model.headerData(item, Qt.Horizontal, Qt.DisplayRole)
            if value == '':
                self.column_values[header] = '-'
            else:
                self.column_values[header] = value