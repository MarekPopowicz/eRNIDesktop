import os
import re
import subprocess
import webbrowser

import psutil
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QDialog

from db import Query
from editors import HTMLEditor
from ui.template_params_form import Ui_Form
from utils import info_boxes, file_io, outlook


class TemplateInspector(QDialog, Ui_Form):
    def __init__(self, manager):
        super().__init__()
        self.setupUi(self)
        self.addressbook = None
        self.localization_manager = manager.localization_manager
        self.current_date = QDate.currentDate().toString(Qt.ISODate)
        self.template_path = ''
        self.repository_path = ''
        self.devices = {}
        self.params = None
        self.editor = None
        self.btn_add_doc.clicked.connect(self.on_add_doc)
        self.btn_del_doc.clicked.connect(self.on_del_doc)
        self.btn_add_attachment.clicked.connect(self.on_add_attachment)
        self.btn_del_attachment.clicked.connect(self.on_del_attachment)
        self.btn_add_localization.clicked.connect(self.on_add_localization)
        self.btn_del_localization.clicked.connect(self.on_del_localization)
        self.btn_ok.clicked.connect(self.on_submit)
        self.document_form = None
        self.correspondence_record = None

    @staticmethod
    def move_items(list_from, list_to):
        items = []
        if len(list_from.selectedItems()) > 0:
            for item in list_from.selectedItems():
                items.append(item.text())
                list_from.takeItem(list_from.row(item))
            list_to.addItems(items)
            items.clear()

    def on_add_doc(self):
        if self.lstwg_docs_tmpl.count() == 0:
            self.move_items(self.lstwg_docs, self.lstwg_docs_tmpl)
        else:
            info_boxes.criticalBox('Niedozwolona operacja', 'Treść szablonu dopuszcza przywołanie tylko jednego dokumentu')

    def on_del_doc(self):
        self.move_items(self.lstwg_docs_tmpl, self.lstwg_docs)

    def on_add_attachment(self):
        self.move_items(self.lstwg_attachments, self.lstwg_attachments_tmpl)

    def on_del_attachment(self):
        self.move_items(self.lstwg_attachments_tmpl, self.lstwg_attachments)

    def on_add_localization(self):
        self.move_items(self.lstwg_localization, self.lstwg_localization_tmpl)

    def on_del_localization(self):
        self.move_items(self.lstwg_localization_tmpl, self.lstwg_localization)

    def get_list_items(self, record, params, doc_type):
        self.params = params
        self.document_form = doc_type
        self.correspondence_record = record
        manager = self.localization_manager.parent

        if doc_type == 'Papier':
            self.template_path = self.localization_manager.parent.settings[0]
        else:
            self.template_path = self.localization_manager.parent.settings[1]
        self.repository_path = self.localization_manager.parent.settings[2]
        # reset controls
        self.lstwg_docs.clear()
        self.lstwg_attachments.clear()
        self.lstwg_localization.clear()
        self.lstwg_docs_tmpl.clear()
        self.lstwg_attachments_tmpl.clear()
        self.lstwg_localization_tmpl.clear()
        self.gbx_docs.setEnabled(False)
        self.sbx_quantity.setEnabled(False)
        self.gbx_attachments.setEnabled(False)
        self.gbx_localizations.setEnabled(False)
        self.set_params(self.correspondence_record[1])

        # gather all documents information onto the list
        documents = []
        for i in range(manager.document_manager.model.rowCount()):
            item = str(i + 1) + ") " + self.get_document_item(i, 'keyDocumentName', manager.document_manager) + \
                   ', nr ' + self.get_document_item(i, 'keyDocumentSign', manager.document_manager) + \
                   ', z dn. ' + self.get_document_item(i, 'keyDocumentDate', manager.document_manager)
            documents.append(item)

        # Limit searching of the documents up to the template parameters type
        if doc_type == 'Papier':
            _params = params[1].split(',')
        else:  # e-mail
            _params = params[3].split(',')

        # add documents to list widget
        if len(documents) > 0:
            for k in range(len(documents)):
                for j in range(len(_params)):
                    if documents[k].find(_params[j].strip()) != -1:
                        self.lstwg_docs.addItem(documents[k].split(') ')[1])
            self.lstwg_attachments.addItems(documents)

        # gather all devices information onto the list
        self.devices.clear()
        localizations = []
        if self.localization_manager.model.rowCount() > 0:
            for i in range(self.localization_manager.model.rowCount()):
                item = '[KW: ' + self.get_document_item(i, 'localizationLandRegister', self.localization_manager) + '] ' \
                                                                                                                    'dz. nr ' + self.get_document_item(
                    i, 'localizationPlotNo', self.localization_manager) + \
                       ', AM-' + str(int(self.get_document_item(i, 'localizationMapNo', self.localization_manager))) + \
                       ', obr. ' + self.get_document_item(i, 'localizationPrecinct', self.localization_manager) + \
                       '; ' + self.get_document_item(i, 'placeName', self.localization_manager)
                localizations.append(item)

                # binds adequate device with its localization
                query = f'SELECT * FROM tblDevices WHERE localizationID = {self.get_document_item(i, "localizationID", self.localization_manager)}'
                device_list = Query.get_data(self.localization_manager.dbase, query, 5)
                if not device_list:
                    info_boxes.criticalBox('Brak informacji', 'Brak informacji o urządzeniach')
                    return
                self.devices[item] = self.get_device_item(device_list)

            # loads localization items into list widget
            for localization in localizations:
                self.lstwg_localization.addItem(localization.split('] ')[1])

        else:
            info_boxes.criticalBox('Brak informacji', 'Brak informacji o lokalizacji')
            return

        self.lstwg_docs.setFocus()
        self.show()

    def set_params(self, tpl_name):
        if self.document_form == 'Papier':
            self.lbl_email_template_name.setVisible(False)
            self.cbx_priority.setVisible(False)
            if self.params[0] == 1: self.gbx_docs.setEnabled(True)  # points on document
            if self.params[2] == 1:  # points on quantity of attachments
                self.lbl_quantity.setVisible(True)
                self.sbx_quantity.setVisible(True)
                self.sbx_quantity.setEnabled(True)
                self.sbx_quantity.setValue(1)
            if self.params[3] == 1: self.gbx_attachments.setEnabled(True)  # points on quantity of attachments
            if self.params[4] == 1: self.gbx_localizations.setEnabled(True)  # points on localization
            self.lbl_template_name.setText(f'Szablon: {tpl_name}')
            self.lbl_type.setText(f'Nawiązuje do: {self.params[1]}')

        else:  # e-mail
            # set controls visibility
            self.lbl_email_template_name.setVisible(True)
            self.lbl_quantity.setVisible(False)
            self.sbx_quantity.setVisible(False)
            self.cbx_priority.setVisible(True)
            self.cbx_priority.setChecked(False)
            if self.params[1] == 1:
                self.cbx_priority.setChecked(True)
            if self.params[2] == 1: self.gbx_docs.setEnabled(True)  # points on document
            if self.params[7] == 1: self.gbx_attachments.setEnabled(True)  # points on attachments list
            if self.params[5] == 1: self.gbx_localizations.setEnabled(True)  # points on localization
            self.lbl_email_template_name.setText(f'Szablon: {tpl_name}')
            self.lbl_template_name.setText(f'Nagłówek: {self.params[0]}')
            self.lbl_type.setText(f'Nawiązuje do: {self.params[3]}')

    @staticmethod
    def get_document_item(row, field_name, manager):
        field = manager.model.fieldIndex(field_name)
        idx = manager.model.index(row, field)
        result = manager.model.data(idx)
        return result

    def get_device_item(self, dev):
        devices = []
        for i in range(len(dev)):
            device_id = dev[i][4]
            device_length = dev[i][1]
            device_width = dev[i][2]
            device_name = self.get_device_name(device_id)
            devices.append({'dł.': device_length, 'szer.': device_width, 'urządzenie': device_name})
        return devices

    def get_device_name(self, device_name_id):
        sql_query = f'SELECT deviceCategoryName FROM tblDeviceCategories WHERE deviceCategoryID = {device_name_id}'
        cat_name = Query.get_data(self.localization_manager.dbase, sql_query, 1)
        return cat_name[0][0]

    def on_submit(self):
        if not self.validate_form(self.check_controls_activity()):
            return

        result = {}
        if self.lstwg_docs_tmpl.count() == 1:
            self.lstwg_docs_tmpl.item(0).setSelected(True)
            d = self.lstwg_docs_tmpl.selectedItems()
            result['documents'] = d
        else:
            result['documents'] = None

        if self.lstwg_attachments_tmpl.count() > 0:
            self.lstwg_attachments_tmpl.selectAll()
            a = self.lstwg_attachments_tmpl.selectedItems()
            result['attachments'] = a
        else:
            result['attachments'] = None

        if self.lstwg_localization_tmpl.count() > 0:
            self.lstwg_localization_tmpl.selectAll()
            l = self.lstwg_localization_tmpl.selectedItems()
            result['localizations'] = l
        else:
            result['localizations'] = None

        if self.document_form == 'Papier':
            result['quantity'] = self.sbx_quantity.value()
            self.print_document(result, self.correspondence_record)
        else:
            result['priority'] = self.cbx_priority.isChecked()
            self.send_email(result, self.correspondence_record)

    def send_email(self, doc_data, record, path=None):
        if path is None:
            path = self.template_path

        if doc_data is not None:
            template_name = self.lbl_email_template_name.text()
            tpl_name = template_name.split(': ')[1] + '.txt'
        else:
            template_name = 'Empty'
            tpl_name = template_name + '.txt'
            self.document_form = 'Email'

        template = file_io.read_file(path + '\\' + tpl_name)

        if template is None:
            info_boxes.criticalBox('Brak szablonu', 'Brak szablonu e-mail.')
            self.localization_manager.parent.correspondence_manager.table.selectRow(0)
            self.close()

            return

        attachments = []
        priority = 1
        if doc_data is not None:
            localization_text = self.get_localization(doc_data['localizations'], 'localization_text')
            devices = self.get_localization(doc_data['localizations'], 'devices')
            document_text = self.get_document(doc_data['documents'], 4)
            attachments_text = self.get_attachment(doc_data['attachments'])
            attachments = self.get_files(doc_data['attachments'])
            priority = doc_data['priority']

            if template.find('[Localization]') > -1:
                if len(localization_text) > 0:
                    localization = ''
                    for item in localization_text:
                        localization += item.split("; ")[0] + ',\n'
                    template = template.replace('[Localization]', localization)

            if template.find('[Localization : Devices]') > -1:
                localization_devices = ''
                if len(devices) > 0:
                    for item in devices:
                        for key, value in item.items():
                            localization_devices += key.split("; ")[0] + ':\n'
                            for dev in value:
                                localization_devices += f"\t■ {dev['urządzenie']}, dł.: {dev['dł.']} m., szer.: {dev['szer.']} m., » pow.: {dev['dł.'] * dev['szer.']} m²\n"
                    template = template.replace('[Localization : Devices]', localization_devices)

            if template.find('[Attachments]') > -1:
                if len(attachments_text) > 0:
                    attachment = ''
                    i = 1
                    for item in attachments_text:
                        item = item.split(') ')[1]
                        attachment += '\t' + str(i) + ') ' + item + '\n'
                        i += 1
                    template = template.replace('[Attachments]', attachment)

            if template.find('[Document]') > -1:
                if len(document_text) > 0:
                    template = template.replace('[Document]', document_text[0])

        manager = self.localization_manager.parent
        case = self.get_document_item(manager.current_row(), 'projectID', manager)
        # sap = self.get_document_item(manager.current_row(), 'projectSapNo', manager)
        path = self.repository_path + '\\' + str(case)

        if template.find('[Case]') > -1:
            template = template.replace('[Case]', str(case))

        if template.find('[Date]') > -1:
            template = template.replace('[Date]', self.current_date)

        if template.find('[Subject]') > -1:
            subject = record[4]
            template = template.replace('[Subject]', subject)

        if template.find('[Foreign_sign]') > -1:
            foreign_sign = self.get_document_item(manager.current_row(), 'projectForeignSignature', manager)
            template = template.replace('[Foreign_sign]', foreign_sign)

        if template.find('[User]') > -1:
            template = template.replace('[User]', self.gather_user_data())

        if template.find('[Corporation]') > -1:
            if not self.gather_corporation_data():
                info_boxes.criticalBox('Brak danych', 'Brakuje informacji o Spółce w ustawieniach aplikacji.')
                return
            template = template.replace('[Corporation]', self.gather_corporation_data())

        if template.find('[Email]') > -1:
            mail = self.localization_manager.parent.settings[9]
            template = template.replace('[Email]', mail)

        if template.find('[Phone]') > -1:
            phone = self.localization_manager.parent.settings[8]
            template = template.replace('[Phone]', phone)

        response = info_boxes.questionBox('Pytanie', 'Czy przygotować wiadomość do wysyłki teraz ?')

        if response == 16384:
            if doc_data is not None:
                sub = self.lbl_template_name.text().split(': ')[1]  # e-mail message subject
            else:
                sub = record[4]

            addressee = record[0]
            email = self.get_email(addressee)

            sign = record[3]
            header = f'{sign}: {sub}'

            # Checking if outlook is already opened. If not, open Outlook.exe
            flag = 0
            try:
                for item in psutil.pids():
                    p = psutil.Process(item)
                    if p.name() == "OUTLOOK.EXE":
                        flag = 1
                        break
                if flag == 1:
                    outlook.send_notification(email, header, template, path, attachments, priority)
                else:
                    info_boxes.informationBox('Outlook', "Aplikacja Outlook jest zamknięta.")
                    self.open_outlook()
                    outlook.send_notification(email, header, template, path, attachments, priority)
            except Exception as error:
                info_boxes.criticalBox("Błąd", f'Wystąpił wyjątek: {type(error).__name__} – {error}')

        self.close()

    def change_phrase(self, words, item, param):
        if self.params[param] == 1:  # jeśli szablon dopuszcza zmianę formy leksykalnej
            for word in words.items():
                if item.find(word[0]) > -1:
                    item = item.replace(word[0], word[1])
        if item.find('nr Brak oznaczenia, ') > -1:
            item = item.replace('nr Brak oznaczenia, ', '')
        return item

    def get_localization(self, doc_data, what):
        localization_text = []
        devices = []
        localizations = doc_data
        if not localizations is None:
            if len(localizations) > 0:
                for item in localizations:  # localizations zawiera pozycje z widgetu listy - zawsze bez KW

                    if self.document_form == 'Papier':
                        if self.params[5] == 0:  # lokalizacja bez KW
                            localization_text.append(item.text())
                            for key, value in self.devices.items():
                                if key.split('] ')[1] == item.text():
                                    devices.append({key.split('] ')[1]: value})
                        else:
                            for key, value in self.devices.items():
                                if key.split('] ')[1] == item.text():
                                    localization_text.append(key)  # lokalizacja z KW
                                    devices.append({key: value})
                    else:  # e-mail
                        if self.params[6] == 0:  # lokalizacja bez KW
                            localization_text.append('■ ' + item.text())
                            for key, value in self.devices.items():
                                if key.split('] ')[1] == item.text():
                                    devices.append({key.split('] ')[1]: value})
                        else:
                            for key, value in self.devices.items():
                                if key.split('] ')[1] == item.text():
                                    localization_text.append(key)  # lokalizacja z KW
                                    devices.append({key: value})
        return {
            'localization_text': localization_text,
            'devices': devices,
        }[what]

    def get_document(self, doc_data, param):
        document_text = []
        document = doc_data
        if not document is None:
            for item in document:
                doc = self.change_phrase({'Protokół': 'protokołu', 'Umowa': 'umowy', 'Aneks': 'aneksu',
                                          'Operat szacunkowy': 'operatu szacunkowego', 'Porozumienie': 'porozumienia'}, item.text(), param)
                document_text.append(doc)
        return document_text


    def initHTML_editor(self, template, template_name, repos_path):
        HTML_editor = HTMLEditor.HTMLEditor(template, template_name, repos_path, self)
        return HTML_editor


    def open_HTML_editor(self, template, template_name, repos_path):
        self.editor = self.initHTML_editor(template, template_name, repos_path)
        self.editor.show()


    @staticmethod
    def get_attachment(doc_data):
        attachments_text = []
        i = 1
        if not doc_data is None:
            for item in doc_data:
                itm = item.text()
                itm = itm.split(') ')[1]
                attachments_text.append(str(i) + ') ' + itm) # re-numerate items
                i+=1
        return attachments_text

    def get_files(self, doc_data):
        files_text = []
        if not doc_data is None:
            for item in doc_data:
                file = self.get_document_item(int(item.text().split(') ')[0]) - 1, 'keyDocumentFile',
                                              self.localization_manager.parent.document_manager)
                files_text.append(file)
        return files_text

    def print_document(self, doc_data, record):
        manager = self.localization_manager.parent

        template_path = self.localization_manager.parent.settings[0]
        repos_path = self.localization_manager.parent.settings[2]

        case = self.get_document_item(manager.current_row(), 'projectID', manager)

        if doc_data is not None:
            template_name = self.lbl_template_name.text()
            tpl_name = template_name.split(': ')[1] + '.tpl'
        else:  # the method has been invoked directly over the constructor
            template_name = 'Empty'
            tpl_name = template_name + '.tpl'
            repos_path += '\\' + str(case)
            self.document_form = 'Papier'

        template = file_io.read_file(template_path + '\\' + tpl_name)

        if template is None:
            info_boxes.criticalBox('Brak szablonu', 'Brak szablonu dokumentu.')
            self.localization_manager.parent.correspondence_manager.table.selectRow(0)
            self.close()
            return

        if doc_data is not None:
            localization_text = self.get_localization(doc_data['localizations'], 'localization_text')
            devices = self.get_localization(doc_data['localizations'], 'devices')
            document_text = self.get_document(doc_data['documents'], 6)
            attachments_text = self.get_attachment(doc_data['attachments'])
            quantity = doc_data['quantity']

            if template.find('[Localization]') > -1:
                if len(localization_text) > 0:
                    localization = ''
                    for item in localization_text:
                        localization += f'<span style="font-weight: bolder; color: red"> &#9679;&nbsp;</span>{item.split("; ")[0]} <br>'
                    template = template.replace('[Localization]', localization)

            if template.find('[Localization : Devices]') > -1:
                localization_devices = ''
                if len(devices) > 0:
                    for item in devices:
                        for key, value in item.items():
                            localization_devices += f'<br><span style="font-weight: bolder; color: red">&#9679;&nbsp;</span>{key.split("; ")[0]}:<br>\n'
                            for dev in value:
                                localization_devices += f"&emsp;&emsp;&#10149; {dev['urządzenie']}, dł.: <strong>{dev['dł.']} m.</strong>, szer.: <strong>{dev['szer.']} m.</strong>, &emsp;pow.: <strong>{dev['dł.'] * dev['szer.']} m<sup>2</sup></strong><br>\n"
                    template = template.replace('[Localization : Devices]', localization_devices)

            if template.find('[Quantity]') > -1:
                if quantity is not None:
                    template = template.replace('[Quantity]', str(quantity))

            if template.find('[Attachments]') > -1:
                if len(attachments_text) > 0:
                    attachment = ''
                    for item in attachments_text:
                        attachment += item + '<br>\n'
                    template = template.replace('[Attachments]', attachment)
                else:
                    template = template.replace('visibility: visible', 'visibility: hidden')

            if template.find('[Document]') > -1:
                if len(document_text) > 0:
                    template = template.replace('[Document]', document_text[0])

            template = template.replace('[Label]', template_name.split(': ')[1])

        template = template.replace('src="td_logo.png"', 'src="../../DocsTempl/Images/td_logo.png"')

        if template.find('[Case]') > -1:
            template = template.replace('[Case]', str(case))

        if template.find('[Date]') > -1:
            template = template.replace('[Date]', self.current_date)

        if template.find('[Subject]') > -1:
            subject = record[4]
            template = template.replace('[Subject]', subject)

        sign = ''
        if template.find('[Sign]') > -1:
            sign = record[3]
            template = template.replace('[Sign]', sign.split(') ')[1])

        if template.find('[Foreign_sign]') > -1:
            foreign_sign = self.get_document_item(manager.current_row(), 'projectForeignSignature', manager)
            template = template.replace('[Foreign_sign]', foreign_sign)
            if foreign_sign == '':
                template = template.replace('#foreign_sign{visibility: visible}', '#foreign_sign{visibility: hidden}')
            else:
                template = template.replace('#foreign_sign{visibility: hidden}', '#foreign_sign{visibility: visible}')

        if template.find('[User]') > -1:
            template = template.replace('[User]', self.gather_user_data())

        if template.find('[Corporation]') > -1:
            if not self.gather_corporation_data():
                info_boxes.criticalBox('Brak danych', 'Brakuje informacji o Spółce w ustawieniach aplikacji.')
                return
            template = template.replace('[Corporation]', self.gather_corporation_data())

        addressee = record[0]
        addressee_data = self.get_addressee_data(addressee)

        if not addressee_data:
            addressee = addressee.replace('\n', '<br>')
            addressee_data = addressee

        template = template.replace('[Addressee]', addressee_data)

        if template.find('[Email]') > -1:
            mail = self.localization_manager.parent.settings[9]
            template = template.replace('[Email]', mail)

        if template.find('[Phone]') > -1:
            phone = self.localization_manager.parent.settings[8]
            template = template.replace('[Phone]', phone)

        if not doc_data is None:
            tpl_name = tpl_name.split('.')[0] + '.htm'
        else:
            tpl_name = self.current_date + ' ' + sign.replace('/', '_') + '.htm'

        if doc_data is None:
            template = template.replace('[Label]', 'Dokument')
            if template.find('[Content]') > -1:
                self.open_HTML_editor(template, tpl_name, repos_path)
                self.close()
                return

        path = repos_path + '\\' + str(case)
        if not file_io.write_file(path + '\\' + tpl_name, template):
            info_boxes.criticalBox('Błąd',
                                   'Dokument nie został zapisany.\n'
                                   'Sprawdź, czy istnieje katalog zadania zgodnie z ustawieniami aplikacji.')
            return

        response = info_boxes.questionBox('Pytanie', 'Czy wydrukować teraz ?')

        if response == 16384:
            webbrowser.open(path + '\\' + tpl_name)
        else:
            info_boxes.informationBox('Informacja', 'Dokument został zapisany w katalogu zadania.')
        self.close()

    def gather_user_data(self):
        name = self.localization_manager.parent.settings[4]
        phone = self.localization_manager.parent.settings[8]
        mail = self.localization_manager.parent.settings[9]

        if self.document_form == 'Papier':
            user_info = f'{name} <br>tel.: {phone} <br>e-mail: {mail}'
        else:
            user_info = f'{name} \ntel.: {phone} \ne-mail: {mail}'
        return user_info

    def gather_corporation_data(self):
        if len(self.localization_manager.parent.settings[11]) > 0:
            name = self.localization_manager.parent.settings[11].split('; ')
            address = self.localization_manager.parent.settings[12].split('; ')
            corporation_info = f'{name[0]} <br>{name[1]} <br>{address[0]}<br>{address[1]}'
            return corporation_info
        else:
            return False

    def get_email(self, addressee):
        table = ''
        if self.addressbook is None:  # search across all address books
            for tbl in ['tblExternalsAddressee', 'tblInternalAddressee', 'tblCollaborativeAddressee']:
                sql_query = f'SELECT * FROM {tbl} WHERE addresseeName = "{addressee}"'
                result = Query.get_data(self.localization_manager.dbase, sql_query, 11)
                if not result:
                    continue
                else:
                    break
        else:
            match self.addressbook:
                case 'Zewnętrzna':
                    table = 'tblExternalsAddressee'
                case 'Wewnętrzna':
                    table = 'tblInternalAddressee'
                case 'Usługodawcy':
                    table = 'tblCollaborativeAddressee'

            sql_query = f'SELECT * FROM {table} WHERE addresseeName = "{addressee}"'
            result = Query.get_data(self.localization_manager.dbase, sql_query, 11)

        if not result:
            sql_query = f'SELECT * FROM tblProjectManagers WHERE projectManager Like "%{addressee}%"'
            result = Query.get_data(self.localization_manager.dbase, sql_query, 4)
            if not result:  # finally
                if self.validate_email(addressee):
                    return addressee
                else:
                    info_boxes.warningBox('Nierozpoznany format',
                                          'Niepoprawny format adresu e-mail\n'
                                          'Dodaj adresata z poziomu klienta poczty e-mail.')
                    return ''  # leave empty e-mail address
            return result[0][3]
        return result[0][8]

    @staticmethod
    def validate_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

    def get_addressee_data(self, addressee_name):
        for addressbook in ['tblExternalsAddressee', 'tblInternalAddressee', 'tblCollaborativeAddressee']:
            sql_query = f'SELECT * FROM {addressbook} WHERE addresseeName = "{addressee_name}"'
            result = Query.get_data(self.localization_manager.dbase, sql_query, 11)
            if not result:
                continue
            else:
                if result[0][1].find(';') > -1:
                    name = result[0][1].split('; ')
                    addressee_info = f'{name[0]}<br>{name[1]}<br>{result[0][10]} {result[0][2]}/{result[0][3]}<br>{result[0][7]} {result[0][6]}'
                else:
                    addressee_info = f'{result[0][1]}<br>{result[0][10]} {result[0][2]}/{result[0][3]}<br>{result[0][7]} {result[0][6]}'
                if result[0][3] == '':
                    addressee_info = addressee_info.replace('/', '')
                return addressee_info
        if not result:
            return result

    def check_controls_activity(self):
        active_controls = []
        if self.lstwg_docs.isEnabled():
            active_controls.append(self.lstwg_docs_tmpl)
        if self.lstwg_attachments.isEnabled():
            active_controls.append(self.lstwg_attachments_tmpl)
        if self.lstwg_localization.isEnabled():
            active_controls.append(self.lstwg_localization_tmpl)
        if self.document_form == 'Papier' and self.sbx_quantity.isEnabled():
            active_controls.append(self.sbx_quantity)
        return active_controls

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
                case 'QListWidget':
                    if not field.item(0):
                        result.append(0)
        if len(result) > 0:
            info_boxes.informationBox("Brak wymaganych informacji",
                                      "Nie wszystkie wymagane pola zostały prawidłowo wypełnione.")
            return False
        else:
            return True

    def open_outlook(self):

        outlook_path = self.localization_manager.parent.settings[17]
        if len(outlook_path) == 0:
            info_boxes.criticalBox('Outlook', "Brak określonej ścieżki dostępu do programu 'Outlook' w ustawieniach aplikacji")
            return
        try:
            subprocess.Popen([outlook_path])
            os.system(outlook_path)
        except:
            info_boxes.criticalBox('Outlook', "Błąd otwarcia aplikacji 'Outlook'")