from PyQt5.QtCore import QModelIndex
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper
from ui.templates_manager import Ui_Form
from utils import info_boxes, file_io


class TemplateManager(QDialog, Ui_Form):
    def __init__(self, dbase):
        super().__init__()
        self.setupUi(self)

        self.model = QSqlTableModel(db=dbase)
        self.model.setTable("tblDocumentsTemplates")
        self.model.select()

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.set_listview_items()
        self.new_index = None

        self.mapper.addMapping(self.txt_template_name, self.model.fieldIndex('documentTemplateName'))
        self.mapper.addMapping(self.txt_description, self.model.fieldIndex('documentTemplateDescription'))
        self.mapper.addMapping(self.txt_doc_service, self.model.fieldIndex('documentType'))
        self.mapper.addMapping(self.txt_info, self.model.fieldIndex('documentAdditionalInfo'))

        self.mapper.addMapping(self.cbx_documents, self.model.fieldIndex('documentTemplateIsPointed'))
        self.mapper.addMapping(self.cbx_quantity_attachements, self.model.fieldIndex('documentQuantity'))
        self.mapper.addMapping(self.cbx_are_attachements, self.model.fieldIndex('documentAnnexesIsPointed'))
        self.mapper.addMapping(self.cbx_localization, self.model.fieldIndex('localizationIsPointed'))
        self.mapper.addMapping(self.cbx_localization_KW, self.model.fieldIndex('localizationLandRegisterIsPointed'))
        self.mapper.addMapping(self.cbx_lexical_forms, self.model.fieldIndex('documentLexicalForms'))

        self.lstvw_templates.selectionModel().selectionChanged.connect(self.on_list_template_changed)

        self.btn_add.clicked.connect(self.add_template)
        self.btn_edit.clicked.connect(self.edit_template)
        self.btn_ok.clicked.connect(self.on_submit)
        self.btn_remove.clicked.connect(self.remove_template)
        self.btn_home_catalog.clicked.connect(self.open_home_folder)
        self.cbx_documents.clicked.connect(self.check_documents)
        self.lbl_template.setText(f'Szablon nr: {self.model.data(self.model.index(0, self.model.fieldIndex("documentTemplateID")))}')
        self.mapper.toFirst()

    @staticmethod
    def open_home_folder():
        settings = file_io.read_encoded('config.txt')
        path = settings[0]
        file_io.open_folder(path)

    def check_documents(self):
        if self.cbx_documents.isChecked() and (
                self.txt_doc_service.toPlainText().find('Brak') > -1 or self.txt_doc_service.toPlainText() == ''):
            info_boxes.warningBox('Niezgodność danych',
                                  'Przy wskazaniu na dokument należy w polu [Przywołuje] określić najpierw jego nazwę')
            self.cbx_documents.setChecked(False)
            self.txt_doc_service.setPlainText('Brak')
            return False
        return True

    def set_listview_items(self, row=0):
        self.lstvw_templates.clear()
        self.model.select()
        if self.model.rowCount() > 0:
            self.btn_edit.setEnabled(True)
            self.btn_remove.setEnabled(True)
            for item in range(self.model.rowCount()):
                val = self.model.data(self.model.index(item, self.model.fieldIndex('documentTemplateName')))
                self.lstvw_templates.addItem(val)
        else:
            self.btn_edit.setEnabled(False)
            self.btn_remove.setEnabled(False)
        self.lstvw_templates.setCurrentRow(row)

    def add_template(self):
        self.btn_add.setEnabled(False)
        self.cbx_documents.setChecked(False)
        self.cbx_lexical_forms.setChecked(False)
        self.cbx_localization.setChecked(False)
        self.cbx_are_attachements.setChecked(False)
        self.cbx_localization_KW.setChecked(False)
        self.cbx_quantity_attachements.setChecked(False)

        row = int(self.model.rowCount())
        self.model.insertRow(row)
        if self.new_index is None:
            self.new_index = QModelIndex(self.model.index(row, 0))
        self.mapper.setCurrentModelIndex(self.new_index)
        self.lstvw_templates.setCurrentIndex(self.new_index)
        self.lstvw_templates.setCurrentRow(self.new_index.row())
        self.btn_edit.setEnabled(False)
        self.btn_remove.setEnabled(False)
        self.txt_doc_service.setPlainText('Brak')
        self.activate_controls()

    def edit_template(self):
        row = self.lstvw_templates.currentIndex().row()
        self.mapper.setCurrentModelIndex(self.model.index(row, 0))
        self.activate_controls()
        self.btn_remove.setEnabled(False)
        self.btn_add.setEnabled(False)

    def remove_template(self):
        if self.model.rowCount() > 0:
            response = info_boxes.questionBox('Usunięcie danych',
                                              'Czy na pewno chcesz trwale usunąć bieżący wiersz ?')
            if response == 16384:
                row = self.lstvw_templates.currentRow()
                self.model.removeRow(row)
                self.set_listview_items()
        self.lstvw_templates.setFocus()

    def on_list_template_changed(self):
        if not self.btn_add.isEnabled():
            self.btn_add.setEnabled(True)
        if not self.btn_edit.isEnabled():
            self.btn_edit.setEnabled(True)
        if not self.btn_remove.isEnabled():
            self.btn_remove.setEnabled(True)

        row = self.lstvw_templates.currentRow()
        idx = self.model.index(row, 0)
        if row is not None:
            self.mapper.setCurrentModelIndex(idx)
            self.deactivate_controls()

        if self.model.data(idx) is not None:
            self.lbl_template.setText(f'Szablon nr: {self.model.data(idx)}')
        else:
            self.lbl_template.setText(f'Szablon nr: nowy')

    def on_submit(self):
        if self.validate_form([self.txt_description, self.txt_template_name, self.txt_doc_service]):
            if self.new_index is not None:
                row = self.new_index.row()
            else:
                row = self.lstvw_templates.currentRow()
            if self.mapper.submit():
                self.model.select()
                self.set_listview_items(row)
                self.new_index = None
                info_boxes.informationBox("Informacja", 'Aktywacja niektórych zmian wymaga restartu aplikacji.')
            else:
                msg = self.model.lastError().text()
                if len(msg) > 0:
                    info_boxes.criticalBox("Błąd", msg)
                else:
                    info_boxes.criticalBox("Błąd", "Coś poszło nie tak.")
        self.deactivate_controls()

    def activate_controls(self):
        self.btn_ok.setEnabled(True)
        self.txt_info.setReadOnly(False)
        self.frm_checkboxes.setEnabled(True)

        self.cbx_documents.setEnabled(True)
        self.cbx_localization.setEnabled(True)
        self.cbx_are_attachements.setEnabled(True)
        self.cbx_quantity_attachements.setEnabled(True)

        self.txt_doc_service.setReadOnly(False)
        self.txt_description.setReadOnly(False)
        self.txt_template_name.setReadOnly(False)
        self.txt_template_name.setFocus()

    def deactivate_controls(self):
        self.btn_ok.setEnabled(False)
        self.txt_info.setReadOnly(True)
        self.frm_checkboxes.setEnabled(False)
        self.txt_doc_service.setReadOnly(True)
        self.txt_description.setReadOnly(True)
        self.txt_template_name.setReadOnly(True)
        self.lstvw_templates.setFocus()

    def validate_form(self, control_list):
        if not self.check_documents():
            return

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