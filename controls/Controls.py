from PyQt5.QtCore import Qt, QDate
from io import StringIO
from utils import info_boxes, file_io
import webbrowser


class Controls:
    def __init__(self, table_manager):
        self.manager = table_manager
        self.current_date = QDate.currentDate().toString(Qt.ISODate)

    def remove_row(self):
        if self.manager.model.rowCount() > 0:
            row = self.manager.table.currentIndex().row()
            if row < 0:
                info_boxes.informationBox('Usunięcie danych',
                                          'Nie wskazano wiersza do usunięcia.')
                return -1

            response = info_boxes.questionBox('Usunięcie danych',
                                              'Czy na pewno chcesz trwale usunąć bieżący wiersz ?')
            if response == 16384:
                self.manager.model.removeRow(row)
                self.manager.select_model()
                if self.manager.model.rowCount() > 0:  # is there any row else ?
                    self.manager.table.selectRow(0)
                    return True
                else:
                    return False

    def print(self, file_name, caption, where=None):
        row_cnt = self.manager.model.rowCount()
        col_cnt = self.manager.model.columnCount()
        if self.manager.__class__.__name__ == 'TaskManager':
            path = self.manager.settings[3]
        else:
            path = self.manager.parent.settings[2] + '\\' + str(where)

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
        <h3  style = "text-shadow: 2px 2px 5px rgb(94, 92, 92);"><span style = "width: 80%; float: left;padding-left: 25px;">[caption]</span> 
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
        report = template.replace('[caption]', caption)
        report = report.replace('[date]', self.current_date)
        content = self.generate_content(row_cnt, col_cnt)
        to_write = report.replace('[report_content]', content.getvalue())
        if file_io.write_file(path + '\\' + file_name + '.htm', to_write):
            webbrowser.open(path + '\\' + file_name + '.htm')
        else:
            info_boxes.criticalBox('Błąd',
                                   'Brak repozytorium.\n'
                                   'Należy utworzyć katalog zgodnie z ustawieniami aplikacji.')

    def generate_content(self, row_count, column_count):
        table = []
        columns_to_hide = []

        # generate table header


        for j in range(column_count):
            col_name = self.manager.model.headerData(j, Qt.Horizontal, Qt.DisplayRole)
            if (self.manager.__class__.__name__ != 'TaskManager') and (col_name == 'Id' or col_name == 'Teczka'):
                columns_to_hide.append(j)
                continue

            if (self.manager.__class__.__name__ == 'ActivityManager') and (col_name == 'Obserwuj'): # hide this column
                columns_to_hide.append(j)
                continue

            table.append(f'<th>{self.manager.model.headerData(j, Qt.Horizontal, Qt.DisplayRole)}</th>\n')
        table.append('</tr>\n')

        # generate table rows
        for i in range(row_count):
            if self.manager.__class__.__name__ == 'TaskManager' and len(self.manager.project_Ids) > 0:  # filter is on
                if not self.manager.model.index(i, 0).data() in self.manager.project_Ids:
                    continue
                else:
                    table.append('<tr>\n')
                    for j in range(column_count):
                        table.append(f'<td>{str(self.manager.model.index(i, j).data())}</td>\n')
                    table.append('</tr>\n')
            else:
                table.append('<tr>\n')
                for j in range(column_count):
                    if j in columns_to_hide:
                        continue
                    table.append(f'<td>{str(self.manager.model.index(i, j).data())}</td>\n')
                table.append('</tr>\n')

        # build content string
        content = StringIO()
        for i in table:
            content.write(i)
        return content

    def get_project_data(self, field_name):
        field = self.manager.parent.model.fieldIndex(field_name)
        idx = self.manager.parent.model.index(self.manager.parent.current_row(), field)
        result = self.manager.parent.model.data(idx)
        return result