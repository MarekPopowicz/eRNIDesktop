import os
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
import ui.html_editor
from db import Query
from editors import TableEditor
from utils import info_boxes, file_io

tags = {'nbsp;': '&nbsp;',
        '<pre>': '</pre>',
        '<p>': '</p>',
        '<br>': '<br>',
        '<span>': '</span>',
        '<div>': '</div>',
        'style=" "': 'style=" "',
        '<!--': '-->',
        '<b>': '</b>',
        '<u>': '</u>',
        '<i>': '</i>',
        '<q>': '</q>',
        '<sup>': '</sup>',
        '<h3>': '</h3>',
        '<ul>': '</ul>',
        '<ol>': '</ol>',
        '<hr>': '<hr>',
        '<table>': '</table>',
        '<caption>': '</caption>',
        '<th>': '</th>',
        '<tr>': '</tr>',
        '<td>': '</td>',
        '<thead>': '</thead>',
        '<tbody>': '</tbody>',
        '<col>': '<col>',
        '<tfoot>': '</tfoot>',
        }


class HTMLEditor(QDialog, ui.html_editor.Ui_Form):
    def __init__(self, template, template_name, repos_path, parent):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # destroy window object on close
        self.path = repos_path
        self.parent = parent
        if self.parent.__class__.__name__ == 'TaskManager':
            self.btn_add.setVisible(False)
            self.btn_edit.setVisible(False)
            self.tab_data.setTabVisible(3, False)
        self.content = template
        self.template = template
        self.template_name = template_name
        self.table_editor = None
        self.table_properties = None
        self.btn_add.clicked.connect(self.on_add)
        self.btn_reset.clicked.connect(self.reset_template)
        self.btn_save_document.clicked.connect(self.save_document)
        self.btn_print.clicked.connect(self.print_content)
        self.btn_edit.clicked.connect(self.edit_document)
        self.btn_load_from_file.clicked.connect(self.load_file)

        self.btn_b.clicked.connect(self.embrace_with_tags)
        self.btn_h3.clicked.connect(self.embrace_with_tags)
        self.btn_p.clicked.connect(self.embrace_with_tags)
        self.btn_q.clicked.connect(self.embrace_with_tags)
        self.btn_u.clicked.connect(self.embrace_with_tags)
        self.btn_br.clicked.connect(self.embrace_with_tags)
        self.btn_col.clicked.connect(self.embrace_with_tags)
        self.btn_comment.clicked.connect(self.embrace_with_tags)
        self.btn_div.clicked.connect(self.embrace_with_tags)
        self.btn_hr.clicked.connect(self.embrace_with_tags)
        self.btn_i.clicked.connect(self.embrace_with_tags)
        self.btn_ol.clicked.connect(self.embrace_with_tags)
        self.btn_ul.clicked.connect(self.embrace_with_tags)
        self.btn_pre.clicked.connect(self.embrace_with_tags)
        self.btn_table.clicked.connect(self.embrace_with_tags)
        self.btn_span.clicked.connect(self.embrace_with_tags)
        self.btn_style.clicked.connect(self.embrace_with_tags)
        self.btn_space.clicked.connect(self.embrace_with_tags)
        self.btn_tbody.clicked.connect(self.embrace_with_tags)
        self.btn_td.clicked.connect(self.embrace_with_tags)
        self.btn_th.clicked.connect(self.embrace_with_tags)
        self.btn_thead.clicked.connect(self.embrace_with_tags)
        self.btn_tfoot.clicked.connect(self.embrace_with_tags)
        self.btn_tr.clicked.connect(self.embrace_with_tags)
        self.btn_sup.clicked.connect(self.embrace_with_tags)
        self.btn_caption.clicked.connect(self.embrace_with_tags)
        self.btn_sap_no.clicked.connect(self.on_data_info_buttons_clicked)
        self.btn_task.clicked.connect(self.on_data_info_buttons_clicked)
        self.btn_localization.clicked.connect(self.on_data_info_buttons_clicked)
        self.btn_devices.clicked.connect(self.on_data_info_buttons_clicked)
        self.btn_localization_devices.clicked.connect(self.on_data_info_buttons_clicked)
        self.btn_documents.clicked.connect(self.on_data_info_buttons_clicked)

        self.txt_content.setPlainText(self.content)

        self.btn_print.setEnabled(False)
        self.btn_add.setEnabled(False)

    def on_data_info_buttons_clicked(self):
        button = self.sender().text()
        cursor = self.txt_content.textCursor()
        data = self.gather_project_information()

        match button:
            case 'Nr zewn.':
                nr = data[0]['ForeignSignature']
                if len(nr) > 0:
                    cursor.insertText(f'<span style = "color: darkblue; font-weight: bold;">{nr}</span>')
                else:
                    info_boxes.informationBox('Brak danych', 'Brak zarejestrowanej sygnatury obcej')

            case 'Zadanie':
                task = data[0]['Task']
                cursor.insertText(f'<span style = "font-style: italic;">{task}</span>')

            case 'Lokalizacja':
                txt = '<ul>\n'
                for item in data[1]:
                    txt += f"\t<li>KW: {item['LandRegister']}, Dz. nr: <strong>{item['PlotNo']}</strong>, AR.<strong>{int(item['MapNo'])}</strong>, Obr. <strong>{item['Precinct']}</strong>; {item['Place']}</li>\n"
                txt += '</ul>\n'
                cursor.insertText(txt)

            case 'Urządzenia':
                txt = '<ul>\n'
                for i in data[2]:
                    for k in i.items():
                        for v in k[1]:
                            txt += f"\t<li>{v['urządzenie']}: Dł.: <strong>{str(v['dł.']).replace('.', ',')}</strong> m., Szer.: <strong>{str(v['szer.']).replace('.', ',')}</strong> m.;  <span style = 'color: darkblue;'>(pow.: <strong>{str(round((v['dł.'] * v['szer.']), 2)).replace('.', ',')}</strong> m<sup>2</sup>)</span></li>\n"
                txt += '</ul>\n'
                cursor.insertText(txt)

            case 'Lok. + Urz.':
                txt = '<ol>\n'
                for localization in data[1]:
                    for i in data[2]:
                        for k in i.items():
                            if localization['ID'] == k[0]:
                                txt += f"\t<li>KW: <strong>{localization['LandRegister']}</strong>, Dz. nr: <strong>{localization['PlotNo']}</strong>, AR.<strong>{int(localization['MapNo'])}</strong>, Obr. <strong>{localization['Precinct']}</strong>; {localization['Place']}:\n"
                                txt += '\t<ul style = "list-style-type:disc";>\n'
                                for v in k[1]:
                                    txt += f"\t\t<li>{v['urządzenie']}: Dł.: <strong>{str(v['dł.']).replace('.', ',')}</strong> m., Szer.: <strong>{str(v['szer.']).replace('.', ',')}</strong> m.;  <span style = 'color: darkblue;'>(pow.: <strong>{str(round((v['dł.'] * v['szer.']), 2)).replace('.', ',')}</strong> m<sup>2</sup>)</span></li>\n"
                                txt += '\t</ul><br>\n'
                txt += '</ol>\n'
                cursor.insertText(txt)

            case 'Dokumenty':
                txt = '<ol>\n'
                for item in data[3]:
                    if item['DocumentSign'] == 'Brak oznaczenia':
                        txt += f"\t<li>{item['DocumentName']}, z dnia {item['DocumentDate']}</li>\n"
                    else:
                        txt += f"\t<li>{item['DocumentName']}, nr: {item['DocumentSign']}, z dnia {item['DocumentDate']}</li>\n"
                txt += '</ol>\n'
                cursor.insertText(txt)

    def gather_project_information(self):
        project = {}
        localizations = []
        devices = []
        documents = []
        manager = self.parent.localization_manager.parent #task manager

        project['Case'] = self.parent.get_document_item(manager.current_row(), 'projectID', manager)
        project['ForeignSignature'] = self.parent.get_document_item(manager.current_row(), 'projectForeignSignature', manager)
        project['SapNumber'] = self.parent.get_document_item(manager.current_row(), 'projectSapNo', manager)
        project['Task'] = self.parent.get_document_item(manager.current_row(), 'projectTask', manager)

        # documents
        for i in range(manager.document_manager.model.rowCount()):
            document_item = {
                'DocumentName': self.parent.get_document_item(i, 'keyDocumentName', manager.document_manager),
                'DocumentSign': self.parent.get_document_item(i, 'keyDocumentSign', manager.document_manager),
                'DocumentDate': self.parent.get_document_item(i, 'keyDocumentDate', manager.document_manager)}
            documents.append(document_item)

        # localizations
        for i in range(manager.localization_manager.model.rowCount()):
            localization_item = {'ID': self.parent.get_document_item(i, 'localizationID', manager.localization_manager),
                                 'LandRegister': self.parent.get_document_item(i, 'localizationLandRegister',
                                                                               manager.localization_manager),
                                 'PlotNo': self.parent.get_document_item(i, 'localizationPlotNo',
                                                                         manager.localization_manager),
                                 'MapNo': self.parent.get_document_item(i, 'localizationMapNo',
                                                                        manager.localization_manager),
                                 'Precinct': self.parent.get_document_item(i, 'localizationPrecinct',
                                                                           manager.localization_manager),
                                 'Place': self.parent.get_document_item(i, 'placeName', manager.localization_manager)}
            localizations.append(localization_item)

            # devices
            query = f'SELECT * FROM tblDevices WHERE localizationID = {localization_item["ID"]}'
            device_list = Query.get_data(manager.dbase, query, 5)
            if not device_list:
                continue
            else:
                device_item = {localization_item['ID']: self.parent.get_device_item(device_list)}
                devices.append(device_item)

        return project, localizations, devices, documents

    def embrace_with_tags(self):
        cursor = self.txt_content.textCursor()
        tag = self.sender().text()
        value = tags[tag]

        if tag == '<table>':
            self.insert_table()
            return

        if tag == '<ol>' or tag == '<ul>':
            self.insert_list(tag, value)
            return

        if value.find('/') > -1 or value.find('--') > -1:
            if cursor.hasSelection():
                new_txt = tag + cursor.selectedText() + value
                cursor.removeSelectedText()
                cursor.insertText(new_txt)
            else:
                txt = tag + value
                cursor.insertText(txt)
        else:
            cursor.insertText(value)

    def insert_table(self):
        if self.table_editor is None:
            self.table_editor = TableEditor.TableEditor(self)
        else:
            self.table_editor.reset_table_properties()
        self.table_editor.show()

    def draw_table(self):
        if not self.table_properties is None:
            cols = self.table_properties['columns']
            rows = self.table_properties['rows']
            caption = self.table_properties['caption']
            footer = self.table_properties['footer']
            header = self.table_properties['header']
            border = self.table_properties['border']
            table = ''

            cell_style = 'style = "border: 1px solid black; border-collapse: collapse;"'
            default_style = 'style = "width: 100%; margin: auto"'
            table_style = 'style = "border: 1px solid black; border-collapse: collapse; width: 100%; margin: auto"'

            table_foot_style = 'style = "background-color: rgb(222, 245, 253); font-weight: bold; text-align: center"'
            table_header_style = 'style = "background-color: rgb(222, 245, 253); font-weight: bold; text-align: center"'

            if (not header) and (not footer):
                if len(caption) > 0:
                    table = f'<table>\n\t<caption>{caption}</caption>'
                else:
                    table = '<table>\n'
                for r in range(rows):
                    table += '<tr>\n'
                    for c in range(cols):
                        table += '\t<td>' + str(r) + '</td>\n'
                    table += '</tr>\n'
                table += '</table>'

            if header and (not footer):
                rows = rows + 1  # one more row for header
                if len(caption) > 0:
                    table = f'<table>\n\t<caption>{caption}</caption>\n\t<thead>\n'
                else:
                    table = '<table>\n\t<thead>\n'
                for r in range(rows):
                    if r == 0:  # header row
                        table += '<tr>\n'
                        for c in range(cols):
                            table += '\t\t<th>' + str(c) + '</th>\n'
                        table += '</tr>\n\t</thead>\n\t<tbody>\n'
                    else:
                        table += '<tr>\n'
                        for c in range(cols):
                            table += '\t\t<td>' + str(r) + '</td>\n'
                        table += '</tr>\n'
                table += '\t</tbody>\n</table>\n'

            if header and footer:
                rows = rows + 1  # one more row for header
                if len(caption) > 0:
                    table = f'<table>\n\t<caption>{caption}</caption>\n\t<thead>\n'
                else:
                    table = '<table>\n\t<thead>\n'
                for r in range(rows):
                    if r == 0:  # header row
                        table += '<tr>\n'
                        for c in range(cols):
                            table += '\t\t<th>' + str(c) + '</th>\n'
                        table += '</tr>\n\t</thead>\n\t<tbody>\n'
                    else:
                        table += '<tr>\n'
                        for c in range(cols):
                            table += '\t\t<td>' + str(r) + '</td>\n'
                        table += '</tr>\n'
                table += '\t</tbody>\n\t<tfoot>\n<tr>\n'

                # footer
                for c in range(cols):
                    table += '\t\t<td>' + str(c) + '</td>\n'
                table += '</tr>\n\t</tfoot>\n</table>'

            if footer and (not header):
                if len(caption) > 0:
                    table = f'<table>\n\t<caption>{caption}</caption>\n\t<tbody>\n'
                else:
                    table = '<table>\n\t<tbody>\n'
                for r in range(rows):
                    table += '<tr>\n'

                    for c in range(cols):
                        table += '\t\t<td>' + str(r) + '</td>\n'

                    table += '</tr>\n'

                table += '\t</tbody>\n\t<tfoot>\n<tr>\n'

                # footer
                for c in range(cols):
                    table += '\t\t<td>' + str(c) + '</td>\n'
                table += '</tr>\n\t</tfoot>\n</table>'

            if not border:
                table = table.replace('<table>', f'<table {table_style}>', 1)
                table = table.replace('<th>', f'<th {cell_style}>')
                table = table.replace('<td>', f'<td {cell_style}>')
                table = table.replace('<tfoot>', f'<tfoot {table_foot_style}>', 1)
                table = table.replace('<thead>', f'<thead {table_header_style}>', 1)
            else:
                table = table.replace('<table>', f'<table {default_style}>', 1)

            cursor = self.txt_content.textCursor()
            cursor.insertText(table)

    def insert_list(self, tag_on, tag_off):
        cursor = self.txt_content.textCursor()
        tag_list = tag_on + '\n' + '\t<li>a...</li>\n' + '\t<li>b...</li>\n' + '\t<li>c...</li>\n' + tag_off
        cursor.insertText(tag_list)

    def print_content(self):
        path = self.path + '\\' + self.template_name
        try:
            webbrowser.open(path)
        except:
            info_boxes.criticalBox('Błąd otwarcia',
                                   'Brak dokumentu.\n'
                                   'Przed wydrukowaniem należy zapisać dokument.')

        self.btn_print.setEnabled(False)

    def on_add(self):
        if self.txt_content.toPlainText().find('<body ') > -1 or self.txt_content.toPlainText().find(
                '<!DOCTYPE html>') > -1 or self.txt_content.toPlainText().find('[Content]') > -1:
            info_boxes.criticalBox('Błąd', 'Próba osadzenia dokumentu w dokumecie')
            return

        if self.content.find('[Content]') == -1:
            response = info_boxes.questionBox('Pytanie', 'Dokument zawiera już zmienioną treść.\n'
                                                         'Czy zastąpić poprzednią treść obecną ?')

            if response == 16384:
                self.content = self.template
                if len(self.txt_content.toPlainText()) > 0:
                    self.content = self.content.replace('[Content]', self.txt_content.toPlainText())
                    # info_boxes.informationBox('Informacja', 'Treść dokumentu została zmieniona.')
                    self.txt_content.setPlainText(self.content)
                    self.btn_save_document.setEnabled(True)
                    return
            else:
                return

            self.btn_add.setEnabled(False)

        if self.content.find('[Content]') > -1:
            if len(self.txt_content.toPlainText()) > 0:
                self.content = self.content.replace('[Content]', self.txt_content.toPlainText())
                info_boxes.informationBox('Informacja', 'Treść dokumentu została zmieniona.')
                self.txt_content.setPlainText(self.content)
                self.btn_save_document.setEnabled(True)
        else:
            info_boxes.criticalBox('Brak znacznika', 'W treści  szblonu brak znacznika [Content]')

    def save_document(self):
        self.content = self.txt_content.toPlainText()
        # show current content within editor window
        self.txt_content.setPlainText(self.content)

        if self.txt_content.toPlainText().find('<body ') == -1 or self.txt_content.toPlainText().find('<!DOCTYPE html>') == -1:
            info_boxes.criticalBox('Błąd', 'Treść dokumentu jest niezgodna ze standardami formtu HTML\n'
                                           'Dokument nie został zapisany.')

            self.btn_print.setEnabled(False)
            return

        if self.template_name is not None:
            path = self.path + '\\' + self.template_name
        else:
            path = file_io.saveFileDialog(self, self.path)
            self.template_name = path.split('/')[-1]
        if not os.path.isdir(self.path):
            file_io.create_folder(self.path)
        if not file_io.write_file(path, self.content):
            info_boxes.criticalBox('Błąd zapisu',
                                   'Coś poszło nie tak. Dokument nie został zapisany.\n'
                                   'Sprawdź, czy istnieje katalog zadania zgodnie z ustawieniami aplikacji.')
            return False

        self.btn_print.setEnabled(True)
        info_boxes.informationBox('Informacja',
                                  'Dokument został zapisany i jest gotowy do wydruku.')
        return True

    def reset_template(self):
        self.btn_add.setEnabled(True)
        self.btn_print.setEnabled(False)
        self.btn_save_document.setEnabled(False)
        self.content = self.template
        self.txt_content.clear()
        info_boxes.informationBox('Informacja',
                                  'Wszystkie wprowadzone zmiany zostały usunięte')
        self.txt_content.setPlainText(self.content)

    def edit_document(self):
        self.btn_add.setEnabled(True)
        self.btn_save_document.setEnabled(False)
        self.btn_print.setEnabled(False)
        self.txt_content.clear()

    def load_file(self):
        file = file_io.get_file(self.path)
        doc = file_io.read_file(file)
        self.txt_content.clear()
        self.txt_content.setPlainText(doc)
        if self.parent.__class__.__name__ == 'TaskManager':
            self.btn_save_document.setEnabled(True)