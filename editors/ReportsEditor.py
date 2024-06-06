import csv
import re
import webbrowser
from io import StringIO
import pandas
from PyQt5.QtCore import Qt, QModelIndex, QItemSelectionModel, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractScrollArea, QDataWidgetMapper
import ui.report_editor
from db import ColumnNames, Query
from utils import file_io, info_boxes, delegates, styles


class ReportsEditor(QDialog, ui.report_editor.Ui_Form):
    def __init__(self, dbase, settings):
        self.column_titles = ColumnNames.reports_table_column_titles
        self.db = dbase
        self.path_reports = settings[3]
        self.user = settings[4]
        self.current_date = QDate.currentDate().toString(Qt.ISODate)
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # destroy window object on close
        align_delegate = delegates.AlignDelegate(self.tbl_reports)

        self.model = QSqlTableModel(db=dbase)
        self.model.setTable("tblReports")
        self.model.select()
        self.tbl_reports.setModel(self.model)

        self.set_table_header_names()
        header = self.tbl_reports.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        header.setDefaultAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        header.setFont(QFont("Tahoma", 10))
        self.tbl_reports.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbl_reports.setFont(QFont("Tahoma", 10))
        self.tbl_reports.setStyleSheet(styles.QHeaderView_qss)
        self.tbl_reports.setItemDelegateForColumn(0, align_delegate)
        self.tbl_reports.setItemDelegateForColumn(4, align_delegate)
        self.cbo_format.addItems(['html', 'xls', 'csv'])

        self.set_edit_controls(True)
        self.tbl_reports.selectionModel().selectionChanged.connect(self.row_changed)
        self.btn_ok.clicked.connect(self.on_submit_clicked)
        self.btn_add.clicked.connect(self.on_add_clicked)
        self.btn_edit.clicked.connect(self.on_edit_clicked)
        self.btn_remove.clicked.connect(self.on_remove_clicked)
        self.btn_print.clicked.connect(self.on_print_clicked)
        self.btn_home.clicked.connect(self.on_home_clicked)

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.addMapping(self.txt_name, self.model.fieldIndex('reportName'))
        self.mapper.addMapping(self.txt_definition, self.model.fieldIndex('reportDefinition'))
        self.mapper.addMapping(self.txt_description, self.model.fieldIndex('reportDescription'))
        self.mapper.addMapping(self.cbo_format, self.model.fieldIndex('reportOutput'))
        self.new_index = None
        self.mapper.toFirst()
        self.btn_ok.setEnabled(False)
        if self.model.rowCount() > 0:
            self.tbl_reports.selectRow(0)
            self.tbl_reports.scrollTo(self.tbl_reports.currentIndex())
        else:
            self.btn_remove.setEnabled(False)
            self.btn_edit.setEnabled(False)
            self.btn_print.setEnabled(False)
            self.cbo_format.setCurrentIndex(-1)

    def set_table_header_names(self):
        for n, t in self.column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Horizontal, t)

    def set_edit_controls(self, isEnabled):
        self.txt_name.setReadOnly(isEnabled)
        self.txt_definition.setReadOnly(isEnabled)
        self.txt_description.setReadOnly(isEnabled)
        self.cbo_format.setEnabled(not isEnabled)

    def clear_controls(self):
        self.txt_name.clear()
        self.txt_definition.clear()
        self.txt_description.clear()
        self.cbo_format.setCurrentIndex(-1)
        self.txt_name.setFocus()

    def on_submit_clicked(self):
        if self.validate_form([self.txt_name, self.txt_description, self.txt_definition, self.cbo_format]):

            if self.mapper.submit():
                self.btn_add.setEnabled(True)
                self.btn_edit.setEnabled(True)
                self.btn_remove.setEnabled(True)
                self.btn_print.setEnabled(True)
                self.btn_ok.setEnabled(False)
                if not self.new_index is None:
                    self.tbl_reports.selectionModel().setCurrentIndex(self.new_index, QItemSelectionModel.ClearAndSelect)
                    self.tbl_reports.selectRow(self.new_index.row())
                    self.new_index = None
            else:
                msg = self.model.lastError().text()
                if len(msg) > 0:
                    info_boxes.criticalBox("Błąd", msg)
                else:
                    info_boxes.criticalBox("Błąd", "Coś poszło nie tak.")
        else:
            return
        self.set_edit_controls(True)
        self.tbl_reports.setFocus()

    def on_add_clicked(self):
        self.btn_ok.setEnabled(True)
        self.btn_edit.setEnabled(False)
        self.btn_remove.setEnabled(False)
        self.set_edit_controls(False)
        self.btn_print.setEnabled(False)
        self.clear_controls()
        row = int(self.model.rowCount())
        self.model.insertRow(row)
        if self.new_index is None:
            self.new_index = QModelIndex(self.model.index(row, 0))
        self.mapper.setCurrentModelIndex(self.new_index)

    def on_edit_clicked(self):
        self.btn_edit.setEnabled(False)
        self.btn_ok.setEnabled(True)
        self.btn_add.setEnabled(False)
        self.btn_print.setEnabled(False)
        self.btn_remove.setEnabled(False)
        self.set_edit_controls(False)
        self.txt_name.setFocus()

    def on_remove_clicked(self):
        if self.model.rowCount() > 0:
            response = info_boxes.questionBox('Usunięcie danych',
                                              'Czy na pewno chcesz trwale usunąć bieżący wiersz ?')
            if response == 16384:
                idx = self.tbl_reports.selectionModel().currentIndex()
                self.model.removeRow(idx.row())
                self.model.select()
                if self.model.rowCount() > 0:
                    new_idx = QModelIndex(self.model.index((idx.row() - 1), 0))
                    self.tbl_reports.selectionModel().setCurrentIndex(new_idx, QItemSelectionModel.ClearAndSelect)
                    self.tbl_reports.selectRow(new_idx.row())
                    self.row_changed()
                else:
                    self.cbo_format.setCurrentIndex(-1)
                    self.btn_ok.setEnabled(False)
                    self.btn_remove.setEnabled(False)
                    self.btn_edit.setEnabled(False)
                    self.btn_print.setEnabled(False)

        self.tbl_reports.setFocus()

    def on_print_clicked(self):
        output = self.cbo_format.currentText()
        sql_command = self.txt_definition.toPlainText()
        pattern = "([']+[\w]+['])"  # pick up each word inside the apostrophes
        result = re.findall(pattern, sql_command)
        columns_name = []
        for item in result:  # get columns aliases from sql command
            item = item.rstrip(item[-1])  # Trim additional apostrophes
            item = item.lstrip(item[0])  # Trim additional apostrophes
            if item == 'now': continue
            columns_name.append(item)
        result = Query.get_rows(self.db, sql_command, columns_name)  # each record is a dict in the list
        if not result:
            info_boxes.criticalBox('Brak danych',
                                   'Brak danych do wydruku lub zapisu raportu.')
            return

        if output == 'html':
            self.html_output(result)
        if output == 'csv':
            self.csv_output(result)
        if output == 'xls':
            self.xls_output(result)

    def html_output(self, data):
        row_count = 0
        col_name_list = []
        if len(data) > 0:
            row_count = len(data)
            col_name_list = list(data[0].keys())
        report_name = self.txt_name.text()
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
            <body>
                <h3  style = "text-shadow: 2px 2px 5px rgb(94, 92, 92);"><span style = "width: 80%; float: left;padding-left: 25px;">[user].  [caption] </span> 
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
        report = report.replace('[user]', self.user)
        report = report.replace('[date]', self.current_date)
        table = [f'<th>Poz.</th>\n']

        # generate table header
        for col in col_name_list:
            table.append(f'<th>{col}</th>\n')
        table.append('</tr>\n')

        # generate table rows
        for row in range(row_count):
            table.append('<tr>\n')
            table.append(f'<td style = "text-align: center">{row+1}</td>\n')
            for item in data[row].items():
                if item[0] == 'Teczka' or item[0] == 'Segment':
                    table.append(f'<td style = "text-align: center">{item[1]}</td>\n')
                elif item[0] == 'Status':
                    td = item[1]
                    if item[1] == 'Wykonany':
                        td = item[1].replace(item[1], '<span style="color: darkblue"><strong>' + item[1] + '</strong></span>')
                    if item[1] == 'Realizacja':
                        td = item[1].replace(item[1], '<span style="color: red">' + item[1] + '</span>')
                    if item[1] == 'Przygotowanie':
                        td = item[1].replace(item[1], '<span style="color: darkgreen">' + item[1] + '</span>')
                    table.append(f'<td style = "text-align: center">{td}</td>\n')
                elif item[0] == 'Lokalizacja':
                    td = item[1].replace('Dz. nr', '◉ Dz. nr ')
                    td = td.replace(';', '<br>')
                    table.append(f'<td>{td}</td>\n')
                elif item[0] == 'Protokoły' or item[0] == 'Protokół':
                    td = item[1].replace('Nr ', '◉ Nr ')
                    td = td.replace(';', '<br>')
                    table.append(f'<td>{td}</td>\n')
                elif item[0] == 'OT' or item[0] == 'Regulacja':
                    td = item[1].replace(';', '<br>')
                    table.append(f'<td>{td}</td>\n')
                elif item[0] == 'Link':
                    if item[1].startswith("https://"):
                        td = item[1].replace(item[1], f'<a href="{item[1]}" target="_blank" rel="noopener noreferrer">Pokaż na mapie</a>')
                        table.append(f'<td>{td}</td>\n')
                    else:
                        table.append(f'<td></td>\n')
                else:
                    table.append(f'<td>{item[1]}</td>\n')

            table.append('</tr>\n')

        # build content string
        content = StringIO()
        for i in table:
            content.write(i)

        to_write = report.replace('[report_content]', content.getvalue())
        if file_io.write_file(self.path_reports + '\\' + report_name + '.htm', to_write):
            webbrowser.open(self.path_reports + '\\' + report_name + '.htm')
        else:
            info_boxes.criticalBox('Błąd zapisu',
                                   'Należy utworzyć katalog raportów zgodnie z ustawieniami aplikacji.')

    def csv_output(self, data):
        # data rows as dictionary objects
        report_name = self.txt_name.text()

        # field names
        col_name_list = list(data[0].keys())

        try:
            with open(self.path_reports + '\\' + report_name + '.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=col_name_list, delimiter='|')
                writer.writeheader()
                writer.writerows(data)
            info_boxes.informationBox('Raport',
                                      'Raport został pomyślnie zapisany.')
        except:
            info_boxes.criticalBox('Błąd zapisu',
                                   'Nie udało się zapisać raportu.')

    # Require installation  of 'xlsxwriter' module (pip install xlsxwriter)
    # Require installation  of 'pandas' module (pip install pandas)
    def xls_output(self, data):
        try:
            report_name = self.txt_name.text()
            df = pandas.DataFrame(data)
            writer = pandas.ExcelWriter(self.path_reports + '\\' + self.user + '_' + report_name + '_' + self.current_date + '.xlsx',
                                        engine='xlsxwriter')
            df.to_excel(writer, sheet_name=self.user, index=False)
            for column in df:
                column_length = max(df[column].astype(str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets[self.user].set_column(col_idx, col_idx, column_length)
            writer.close()

            info_boxes.informationBox('Raport',
                                      'Raport został pomyślnie zapisany.')
        except:
            info_boxes.criticalBox('Błąd zapisu',
                                   'Nie udało się zapisać raportu.')

    @staticmethod
    def on_home_clicked():
        settings = file_io.read_encoded('config.txt')
        path = settings[3]
        file_io.open_folder(path)

    def row_changed(self):
        idx = self.tbl_reports.selectionModel().currentIndex()
        self.mapper.setCurrentIndex(idx.row())

    @staticmethod
    def validate_form(control_list):
        result = []
        for field in control_list:
            match field.__class__.__name__:
                case 'QComboBox':
                    if not field.currentText():
                        result.append(0)
                case 'QPlainTextEdit':
                    if not field.toPlainText():
                        result.append(0)
                case 'QDoubleSpinBox':
                    if field.value() == 0:
                        result.append(0)
                case 'QSpinBox':
                    if field.value() == 0:
                        result.append(0)
                case 'QLineEdit':
                    if not field.text():
                        result.append(0)
        if len(result) > 0:
            info_boxes.informationBox("Brak wymaganych informacji!",
                                      "Nie wszystkie wymagane pola zostały prawidłowo wypełnione.")
            return False
        else:
            return True