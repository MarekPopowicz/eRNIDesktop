import webbrowser
from io import StringIO

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractScrollArea
from prettytable import PrettyTable

import ui.todo_list_form
from db import ColumnNames, Query
from mappers import ToDoMapper
from utils import file_io, info_boxes, delegates, styles


class ToDoItemsEditor(QDialog, ui.todo_list_form.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.table = self.tbl_todo_items

        align_delegate = delegates.AlignDelegate(self.tbl_todo_items)
        self.column_titles = ColumnNames.todo_table_column_titles
        self.dbase = parent.dbase

        self.current_date = QDate.currentDate().toString(Qt.ISODate)

        self.model = QSqlTableModel(db=self.dbase)
        self.model.setTable("tblToDo")
        self.model.setSort(4, Qt.AscendingOrder)
        self.model.select()
        self.table.setModel(self.model)
        if self.model.rowCount() > 0:
            self.table.setCurrentIndex(self.model.index(0, 0))
            self.set_buttons(True)
        else:
            self.set_buttons(False)

        self.set_table_header_names()
        header = self.tbl_todo_items.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        header.setDefaultAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        header.setFont(QFont("Tahoma", 10))
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setFont(QFont("Tahoma", 10))
        self.table.setStyleSheet(styles.QHeaderView_qss)
        self.table.setItemDelegateForColumn(1, align_delegate)
        self.table.setItemDelegateForColumn(2, align_delegate)
        self.table.setItemDelegateForColumn(4, align_delegate)
        self.table.setColumnHidden(0, True)
        self.table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.btn_edit.clicked.connect(self.on_edit)
        self.btn_remove.clicked.connect(self.on_remove)
        self.btn_print.clicked.connect(self.on_print_clicked)
        self.todo_mapper = None

    def on_edit(self):
        self.todo_mapper = ToDoMapper.ToDo(self)
        idx = self.table.selectionModel().currentIndex()
        self.todo_mapper.edit_row(idx)
        self.todo_mapper.show()

    def set_table_header_names(self):
        for n, t in self.column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Horizontal, t)

    def on_remove(self):
        if self.model.rowCount() > 0:
            row = self.table.currentIndex().row()
            if row < 0:
                info_boxes.informationBox('Usunięcie danych',
                                          'Nie wskazano wiersza do usunięcia.')
                return
            response = info_boxes.questionBox('Usunięcie danych',
                                              'Czy na pewno chcesz trwale usunąć bieżący wiersz ?')
            if response == 16384:
                self.model.removeRow(row)
                self.model.select()
                if self.model.rowCount() > 0:  # is there any row else ?
                    self.table.selectRow(0)
                else:
                    self.set_buttons(False)

    def set_buttons(self, state):
        self.btn_remove.setEnabled(state)
        self.btn_edit.setEnabled(state)
        self.btn_print.setEnabled(state)

    def on_print(self):
        x = PrettyTable()

        headers = []
        for item in range(len(self.column_titles)):
            header = self.model.headerData(item, Qt.Horizontal, Qt.DisplayRole)
            if item == 0: continue
            headers.append(header)
        x.field_names = headers
        x.align["Do zrobienia"] = "l"

        values = []
        for row in range(self.model.rowCount()):
            values.clear()
            for item in range(len(self.column_titles)):
                if item == 0: continue
                idx = self.model.index(row, item)
                value = self.model.data(idx)
                values.append(value)
            x.add_row(values)
        print(x)

    def on_print_clicked(self):
        sql_command = "SELECT todoTaskCase as 'Teczka', todoRegistrationDate as 'Wpis', todoItem as 'Czynność', todoDeadLine as 'Termin' FROM tblToDo ORDER BY todoDeadLine"
        result = Query.get_rows(self.dbase, sql_command, ['Teczka', 'Wpis', 'Czynność', 'Termin'])  # each record is a dict in the list
        if not result:
            info_boxes.criticalBox('Brak danych',
                                   'Brak danych do wydruku lub zapisu raportu.')
            return

        self.html_output(result)

    def html_output(self, data):
        row_count = 0
        col_name_list = []
        if len(data) > 0:
            row_count = len(data)
            col_name_list = list(data[0].keys())
        report_name = 'Do zrobienia'
        template = '''
           <!DOCTYPE html>
           <html lang="pl-PL">
               <head>
                   <meta charset="UTF-8">
                   <meta name="viewport" content="width=device-width, initial-scale=1.0">
                   <title>Raport</title>
                    <style>
                       table {box-shadow: 5px 5px 5px rgb(204, 199, 199);}
                       table, th, td {border: 1px solid rgb(133, 133, 133); border-collapse: collapse; padding: 5px;}
                       th {text-shadow: 2px 2px 5px rgb(94, 92, 92);}
                       tr:nth-child(even) {background-color: #f0f0f0;}
                       tr:hover {background-color: #dbd8ff;}
                       body {font-family: Verdana, Geneva, Tahoma, sans-serif; font-size: 14px;}
                   </style>
               </head>
               <body onload="window.print()">
                   <h3  style = "text-shadow: 2px 2px 5px rgb(94, 92, 92);"><span style = "width: 80%; float: left;padding-left: 25px;">[caption] </span> 
                       <span style = "width: 10%;">[date]</span>
                   </h3>
                   <table style="width:100%">
                   <tr style = "background-color: #d8d8d8">
                       [report_content]
                   </tr>
                   </table>
               </body>
           </html>
           '''
        report = template.replace('[caption]', report_name)
        report = report.replace('[date]', self.current_date)
        table = []

        # generate table header
        for col in col_name_list:
            table.append(f'<th>{col}</th>\n')
        table.append('</tr>\n')

        # generate table rows
        for row in range(row_count):
            table.append('<tr>\n')
            for item in data[row].items():
                if item[0] == 'Teczka' or item[0] == 'Wpis' or item[0] == 'Termin':
                    table.append(f'<td style = "text-align: center">{item[1]}</td>\n')
                else:
                    table.append(f'<td>{item[1]}</td>\n')

            table.append('</tr>\n')

        # build content string
        content = StringIO()
        for i in table:
            content.write(i)

        to_write = report.replace('[report_content]', content.getvalue())
        if file_io.write_file(report_name + '.htm', to_write):
            webbrowser.open(report_name + '.htm')
        else:
            info_boxes.criticalBox('Błąd zapisu',
                                   'Należy utworzyć katalog raportów zgodnie z ustawieniami aplikacji.')