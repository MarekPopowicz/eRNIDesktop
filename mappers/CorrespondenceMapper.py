from PyQt5.QtCore import Qt, QEvent, QDate
from PyQt5.QtWidgets import QDialog
from db import Query
from inspectors import AddresseeInspector, TemplateInspector
from managers import AddressBookManager
from mappers import Mapper
from ui.correspondence_mapper import Ui_Form
from utils import info_boxes


class CorrespondenceMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, index=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)
        Mapper.Mapper.__init__(self, manager, index, controls)
        self.setupUi(self)
        self.direction = 'Przychodząca'
        self.txt_info.installEventFilter(self)
        self.txt_signature.installEventFilter(self)
        self.set_mapping()
        self.addressbook = AddressBookManager.AddresseeManager(self.manager.dbase, None)
        self.addressee_inspector = None
        self.template_inspector = None
        self.set_header_info(self.lbl_projectId, self.lbl_task_name)
        self.rdb_incoming_post.toggled.connect(self.on_rdb_clicked)
        self.rdb_outcoming_post.toggled.connect(self.on_rdb_clicked)
        self.btn_addressbook.clicked.connect(self.addressbook_open)
        self.btn_addressee_inspector.clicked.connect(self.addressee_inspector_open)
        self.btn_ok.clicked.connect(self.on_submit)
        self.btn_save.clicked.connect(self.on_save)
        self.cbo_type.currentTextChanged.connect(self.on_type_changed)
        self.btn_restore.clicked.connect(self.on_restore)
        self.counter = 0
        self.launch_controls = controls

    def set_correspondence_direction(self):
        self.counter = Query.get_max_id_value(self.manager.dbase, 'tblProjectCorrespondence', 'projectCorrespondenceID')
        if self.counter == '':
            self.counter = 0

        if self.index is not None:
            index = self.model.index(self.current_row, self.model.fieldIndex("projectCorrespondenceDirection"))
            direction = self.model.data(index)

            if direction == 'Przychodząca':
                self.rdb_incoming_post.setChecked(True)
                self.cbo_template.setEnabled(False)
            else:
                self.rdb_outcoming_post.setChecked(True)
                self.cbo_template.setEnabled(True)
            self.cbo_addressee.setCurrentIndex(-1)

            index = self.model.index(self.current_row, self.model.fieldIndex("projectCorrespondenceTemplate"))
            template = self.model.data(index)
            if template == '':
                self.cbo_template.setCurrentIndex(-1)
            else:
                self.cbo_template.setCurrentText(template)
        else:
            self.model.setData(self.model.index(self.current_row, self.model.fieldIndex("projectCorrespondenceDirection")), self.direction)
            self.rdb_incoming_post.setChecked(True)
            self.cbo_template.setEnabled(False)
            self.cbo_template.setCurrentIndex(-1)
            self.dta_correspondence_date.setDate(self.manager.current_date)
            self.dta_inflow_data.setDate(self.manager.current_date)

    def set_mapping(self):
        self.cbo_addressee.addItems(['Zewnętrzna', 'Wewnętrzna', 'Usługodawcy'])
        self.cbo_type.addItems(['Papier', 'Email'])
        self.add_mapping(self.cbo_type, "projectCorrespondenceType")
        self.add_mapping(self.txt_name, "projectCorrespondenceSender")
        self.add_mapping(self.cbo_template, "projectCorrespondenceTemplate")
        self.fill_combo(self.manager.dbase, 'tblDocumentsTemplates', 'documentTemplateName', self.cbo_template)
        self.add_mapping(self.dta_correspondence_date, "projectCorrespondenceDate")
        self.add_mapping(self.txt_signature, "projectCorrespondenceSign")
        self.add_mapping(self.txt_case_description, "projectCorrespondenceSubject")
        self.add_mapping(self.dta_inflow_data, "projectCorrespondenceObtainment")
        self.add_mapping(self.txt_info, "projectCorrespondenceInfo")

    def template_inspector_open(self, tpl_params, doc_type, record):
        if self.template_inspector is None:
            self.template_inspector = TemplateInspector.TemplateInspector(self.manager.parent)

        # set addressbook for template inspector
        if len(self.txt_name.toPlainText()) > 0:
            for item in ['tblExternalsAddressee', 'tblInternalAddressee', 'tblCollaborativeAddressee']:
                sql_query = f'SELECT * FROM {item} WHERE addresseeName = "{self.txt_name.toPlainText()}"'
                result = Query.get_data(self.manager.dbase, sql_query, 11)
                if not result:
                    continue
                else:
                    match item:
                        case 'tblExternalsAddressee':
                            self.cbo_addressee.setCurrentText('Zewnętrzna')
                        case 'tblInternalAddressee':
                            self.cbo_addressee.setCurrentText('Wewnętrzna')
                        case 'tblCollaborativeAddressee':
                            self.cbo_addressee.setCurrentText('Usługodawcy')
                    self.template_inspector.addressbook = self.cbo_addressee.currentText()
                    break

        self.template_inspector.get_list_items(record, tpl_params, doc_type)  # here template_inspector show()

    def addressee_inspector_open(self):
        if self.cbo_addressee.currentIndex() == -1:
            info_boxes.informationBox('Brak wskazania', 'Należy najpierw wybrać typ korespondecji z listy')
            return
        if self.addressee_inspector is None:
            self.addressee_inspector = AddresseeInspector.AddresseeInspector(self.manager.dbase, parent=self)
        self.addressee_inspector.set_position()

        if self.cbo_addressee.currentText() == 'Zewnętrzna':
            table = 'tblExternalsAddressee'
        elif self.cbo_addressee.currentText() == 'Wewnętrzna':
            table = 'tblInternalAddressee'
        else:
            table = 'tblCollaborativeAddressee'

        self.addressee_inspector.load_data(table)
        self.btn_addressee_inspector.hide()
        self.addressee_inspector.show()

    def addressbook_open(self):
        if self.cbo_addressee.currentIndex() == -1:
            info_boxes.informationBox('Brak wskazania', 'Należy najpierw wybrać typ korespondecji z listy')
            return
        if self.cbo_addressee.currentText() == 'Zewnętrzna':
            self.addressbook.show_addressbook('external')
        elif self.cbo_addressee.currentText() == 'Wewnętrzna':
            self.addressbook.show_addressbook('internal')
        else:
            self.addressbook.show_addressbook('servants')

    def on_rdb_clicked(self):
        if self.rdb_incoming_post.isChecked():
            self.direction = 'Przychodząca'
            self.model.setData(self.model.index(self.current_row, self.model.fieldIndex("projectCorrespondenceDirection")), self.direction)
            self.txt_signature.clear()
            self.txt_case_description.clear()
            self.cbo_template.setEnabled(False)
            self.btn_ok.setEnabled(False)
        else:
            self.direction = 'Wychodząca'
            self.model.setData(self.model.index(self.current_row, self.model.fieldIndex("projectCorrespondenceDirection")), self.direction)
            if self.index is None:
                self.txt_signature.setText(f'{self.lbl_projectId.text()}/{self.counter + 1}/{self.manager.current_date.year()}')
            self.cbo_template.setEnabled(True)
            self.btn_ok.setEnabled(True)
            localization_data = self.get_localization_data(self.manager.parent.localization_manager.model.rowCount())
            localization_str = self.set_localization_data(localization_data)
            if not localization_str:
                self.txt_case_description.setPlainText(f'{self.lbl_task_name.text()}')
            else:
                self.txt_case_description.setPlainText(f'{self.lbl_task_name.text()} na {localization_str}')
        self.cbo_template.setCurrentIndex(-1)

    def open_empty_template(self, doc_type, record):
        if self.template_inspector is None:
            self.template_inspector = TemplateInspector.TemplateInspector(self.manager.parent)

        response = info_boxes.questionBox('Pytanie', 'Nie wybrano żadnego z dostępnych szablonów.\n '
                                                     'Czy zastosować pusty szablon ?')
        if response == 16384:
            self.close()

            if doc_type == 'Email':
                template_path = self.manager.parent.settings[1]
                self.template_inspector.send_email(None, record, template_path)
            else:
                self.template_inspector.print_document(None, record)
                return
        else:
            return False

    def on_save(self):
        if self.validate_form([self.txt_name, self.txt_case_description, self.txt_signature]):
            if self.mapper.submit():
                if not self.manager.parent.tabs_case_segments.isTabEnabled(2):
                    self.manager.parent.tabs_case_segments.setTabEnabled(2, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(2)
                    self.results.clear()
                self.btn_restore.setEnabled(False)
            else:
                self.model_last_error_msg()
                self.catch_data()
                self.btn_restore.setEnabled(True)
            self.close()
            return

    def on_submit(self):
        if self.validate_form([self.txt_name, self.txt_case_description, self.txt_signature]):

            record = (self.txt_name.toPlainText(),
                      self.cbo_template.currentText(),
                      self.dta_correspondence_date.date().toString(Qt.ISODate),
                      self.txt_signature.text(),
                      self.txt_case_description.toPlainText(),
                      self.dta_inflow_data.date().toString(Qt.ISODate))

            if self.mapper.submit():
                self.results.clear()
                self.btn_restore.setEnabled(False)
                if not self.manager.parent.tabs_case_segments.isTabEnabled(2):
                    self.manager.parent.tabs_case_segments.setTabEnabled(2, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(2)

                if self.direction == 'Przychodząca' or self.rdb_incoming_post.isChecked() is True:
                    self.close()
                    return

                # template
                if ((self.cbo_type.currentText() == 'Papier' and self.cbo_template.currentIndex() != -1) or
                        (self.cbo_type.currentText() == 'Email' and self.cbo_template.currentIndex() != -1)):
                    template_params = self.get_template_information(self.cbo_template.currentText(), self.cbo_type.currentText())
                    if template_params is not None and len(template_params) > 0:
                        self.template_inspector_open(template_params, self.cbo_type.currentText(), record)

                # empty template
                if ((self.cbo_type.currentText() == 'Papier' and self.cbo_template.currentIndex() == -1) or
                        (self.cbo_type.currentText() == 'Email' and self.cbo_template.currentIndex() == -1)):
                    if not self.open_empty_template(self.cbo_type.currentText(), record):
                        return
            else:
                self.model_last_error_msg()
                self.catch_data()
                self.btn_restore.setEnabled(True)
        else:
            return
        self.close()

    def catch_data(self):
        self.results.clear()
        self.results.append(self.txt_name.toPlainText())
        self.results.append(self.cbo_template.currentText())
        self.results.append(self.dta_correspondence_date.date().toString())
        self.results.append(self.txt_signature.text())
        self.results.append(self.txt_case_description.toPlainText())
        self.results.append(self.dta_inflow_data.date().toString())
        self.results.append(self.direction)
        self.results.append(self.txt_info.toPlainText())
        self.results.append(self.cbo_addressee.currentText())
        self.results.append(self.cbo_type.currentText())

    def on_restore(self):
        self.txt_name.setPlainText(self.results[0])
        self.txt_info.setPlainText(self.results[7])
        self.dta_correspondence_date.setDate(QDate.fromString(self.results[2]))
        self.txt_signature.setText(self.results[3])
        self.txt_case_description.setPlainText(self.results[4])
        self.dta_inflow_data.setDate(QDate.fromString(self.results[5]))
        if self.results[6] == 'Przychodząca':
            self.rdb_incoming_post.setChecked(True)
        else:
            self.rdb_outcoming_post.setChecked(True)
        self.cbo_template.setCurrentText(self.results[1])
        self.cbo_addressee.setCurrentText(self.results[8])
        self.cbo_type.setCurrentText(self.results[9])


    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if source is self.txt_info and (event.key() == Qt.Key.Key_Escape):
                cursor = self.txt_info.textCursor()
                cursor.insertText('Zarejestrowano w SOD pod nr.: ')
            if source is self.txt_signature and (event.key() == Qt.Key.Key_Escape):
                self.txt_signature.setText('Brak oznaczenia')
        return super(CorrespondenceMapper, self).eventFilter(source, event)

    def get_template_information(self, template, _type):
        try:
            if _type == 'Papier':
                sql = f'SELECT * from tblDocumentsTemplates WHERE documentTemplateName = "{template}"'
                tpl = Query.get_data(self.manager.dbase, sql, 11)
                document = tpl[0][2]  # points on document
                doc_type = tpl[0][4]  # points on document type
                quantity = tpl[0][5]  # points on quantity of docs
                annexes = tpl[0][6]  # points on attachments list for current document
                localization = tpl[0][7]  # points on localization
                land_reg = tpl[0][9]  # points on land register
                lex_forms = tpl[0][10]  # points on usage of lexical forms of type document
                return [document, doc_type, quantity, annexes, localization, land_reg, lex_forms]
            else:  # e-mail
                sql = f'SELECT * from tblEmailTemplates WHERE templateName = "{template}"'
                tpl = Query.get_data(self.manager.dbase, sql, 10)
                header = tpl[0][2]  # e-mail subject
                priority = tpl[0][3]  # points on message importance flag
                document = tpl[0][4]  # points on document
                doc_type = tpl[0][5]  # points on document type
                lex_forms = tpl[0][6]  # points on usage of lexical forms of type document
                localization = tpl[0][7]  # points on localization
                land_reg = tpl[0][8]  # points on land register
                annexes = tpl[0][9]  # points on attachments list for current document
                return [header, priority, document, doc_type, lex_forms, localization, land_reg, annexes]
        except:
            info_boxes.informationBox('Brak nazwy', 'Po dokonaniu zmiany nazwy szablonu należy ponownie uruchomić aplikację.')

    def on_type_changed(self):
        self.cbo_template.clear()
        if self.cbo_type.currentText() == 'Papier':
            self.fill_combo(self.manager.dbase, 'tblDocumentsTemplates', 'documentTemplateName', self.cbo_template)
        else:
            self.fill_combo(self.manager.dbase, 'tblEmailTemplates', 'templateName', self.cbo_template)