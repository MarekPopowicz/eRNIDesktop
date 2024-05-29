import json
import os
import subprocess as sp
import sys
import time
import webbrowser
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QEvent, QMetaObject
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QDialog

import ui.splash_screen
from controls import TaskControls, LocalizationControls, DeviceControls, DocumentControls, CorrespondenceControls, \
    ActivityControls, InvoiceControls, RegulationControls, PropertyDocumentControls
from db import ColumnNames, DbCreate, Query, DbData, DbDefinition
from editors import ReportsEditor, ToDoItemsEditor, BatchProcessingReportsEditor
from inspectors import SettingsInspector, TemplateInspector
from managers import DeviceManager, ActivityManager, DocumentManager, CorrespondenceManager, LocalizationManager, \
    TaskManager, InvoiceManager, RegulationManager, PropertyDocumentManager, TaskDetailsManager, TemplateManager, DictionaryManager, \
    AddressBookManager, MailTemplateManager, ProjectManager
from mappers import ToDoMapper
from ui.main_form import Ui_MainWindow
from ui.password_form import Ui_Form
from utils import file_io
from utils import styles, info_boxes

basedir = os.path.dirname(__file__)


class SplashScreen(QDialog, ui.splash_screen.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # destroy window object on close
        self.db = None
        self.state = self.db_connection()

    def db_connection(self):
        dbase = QSqlDatabase("QSQLITE")

        home = os.path.expanduser("~") + '\\eRNI'
        if not os.path.isdir(home):
            file_io.create_folder(home)
            file_io.create_folder(home + '\\Base')
        home += '\\Base'
        db_path = os.path.join(home, "erni.db")
        dbase.setDatabaseName(db_path)

        if dbase.open():
            self.db = dbase
        else:
            info_boxes.criticalBox("Baza danych", "Wystąpił problem z otwarciem bazy danych")
            sys.exit(-1)
        db_content = dbase.tables()
        if len(db_content) == 0:  # Empty database
            if DbCreate.create_database(dbase):
                self.create_shortcuts()
                self.create_notebook()
                self.create_settings()
                self.add_templates()
                self.get_reports_data()
                return True
            else:
                info_boxes.criticalBox("Baza danych", "Wystąpił problem z utworzeniem struktury bazy danych")
                sys.exit(-1)
        else:
            return False

    def get_dictionary_data(self):

        for key, values in DbData.dictionary_tables.items():
            table = key.split('_')[0]
            column = key.split('_')[1]
            minimum = 0
            self.prb_progress.setMinimum(minimum)
            self.prb_progress.setMaximum(len(values))
            info = f"Trwa zapis danych do tabeli słownika: '{table}'"
            self.lbl_progress.setText(info)
            counter = 0
            for value in values:
                sql_command = f"INSERT INTO {table} ({column}) VALUES('{value}')"
                Query.add_value(self.db, sql_command)
                counter += 1
                self.prb_progress.setValue(counter)

    def get_reports_data(self):
        table = 'tblReports'
        columns = 'reportName, reportDefinition, reportDescription, reportOutput'
        # 1
        values = f'"Rejestr prowadzonych spraw", "{DbDefinition.main_report}", "Główny raport OMI", "html"'
        sql_command = f'INSERT INTO {table} ({columns}) VALUES({values})'
        Query.add_value(self.db, sql_command)
        # 2
        values = f'"Czynności obserwowane", "{DbDefinition.actions_to_observe}", "Rejestr czynności wymagających dalszej uwagi", "html"'
        sql_command = f'INSERT INTO {table} ({columns}) VALUES({values})'
        Query.add_value(self.db, sql_command)

    @staticmethod
    def create_settings():
        if DbCreate.create_folders():
            home = os.path.expanduser("~")
            content = ''
            content += file_io.base64_encode(home + '\\eRNI\\DocsTempl') + '\n'
            content += file_io.base64_encode(home + '\\eRNI\\MailTempl') + '\n'
            content += file_io.base64_encode(home + '\\eRNI\\Repos') + '\n'
            content += file_io.base64_encode(home + '\\eRNI\\Reports') + '\n'

            content += file_io.base64_encode('Marek Popowicz') + '\n'
            content += file_io.base64_encode('Specjalista ds. regulacji terenowo-prawnych') + '\n'
            content += file_io.base64_encode('Wydział Inwestycji') + '\n'
            content += file_io.base64_encode('pl. Powstańców Śląskich 20; 53-314 Wrocław') + '\n'
            content += file_io.base64_encode('(071) 889-26-55') + '\n'
            content += file_io.base64_encode('marek.popowicz@tauron-dystrybucja.pl') + '\n'
            content += '\n'  # password

            content += file_io.base64_encode('TAURON Dystrybucja S.A.; Oddział we Wrocławiu') + '\n'
            content += file_io.base64_encode('pl. Powstańców Śląskich 20; 53-314 Wrocław') + '\n'
            content += file_io.base64_encode('6110202860') + '\n'  # NIP
            content += file_io.base64_encode('230179216') + '\n'  # REGON
            content += file_io.base64_encode('0000073321') + '\n'  # KRS
            content += file_io.base64_encode('560 467 130,62 zł') + '\n'  # Kapitał

            content += file_io.base64_encode('C:\\ProgramFiles\\MicrosoftOffice\\Office16\\Outlook.exe') + '\n'
            content += file_io.base64_encode(basedir + '\\shortcuts.json')
            file_io.write_file(basedir + '\\config.txt', content)

    @staticmethod
    def create_shortcuts():
        data = DbData.shortcuts
        # Serializing json
        json_object = json.dumps(data, indent=4)
        file_io.write_file(basedir + '\\shortcuts.json', json_object)

    @staticmethod
    def create_notebook():
        home = os.path.expanduser("~")
        file_io.write_file(home + '\\eRNI\\DocsTempl\\notebook.txt', '')

    @staticmethod
    def add_templates():
        home = os.path.expanduser("~")
        # label_templ = DbData.label
        # file_io.write_file(home + '\\eRNI\\DocsTempl\\label.tpl', label_templ)
        document_template = DbData.document_empty_template
        file_io.write_file(home + '\\eRNI\\DocsTempl\\Empty.tpl', document_template)
        information = DbData.info
        file_io.write_file(home + '\\eRNI\\DocsTempl\\info.txt', information)
        email_template = DbData.email_empty_template
        file_io.write_file(home + '\\eRNI\\MailTempl\\Empty.txt', email_template)


class PasswordControl(QDialog, Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_ok.clicked.connect(self.on_submit)
        try:
            if len(parent.tasks_manager.settings) == 0 or len(parent.tasks_manager.settings[10]) == 0:
                parent.showMaximized()
            else:
                self.show()
        except:
            info_boxes.criticalBox('Błąd krytyczny', 'Brak informacji konfiguracyjnych uniemożliwia dalszą pracę aplikacji')
            QMetaObject.invokeMethod(self, "close", Qt.QueuedConnection)

    def on_submit(self):
        self.close()
        if len(self.parent.tasks_manager.settings[10]) > 0:
            password = self.parent.tasks_manager.settings[10]
            user_input = self.txt_password.text()
            if user_input == password:
                self.parent.showMaximized()
            else:
                info_boxes.criticalBox('Zabezpieczenie', 'Podane hasło jest nierprawidłowe')
                QMetaObject.invokeMethod(self, "close", Qt.QueuedConnection)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, dbase):
        super().__init__()
        self.setupUi(self)

        self.dbase = dbase
        self.regulation_document_controls = None
        self.regulation_controls = None
        self.invoice_controls = None
        self.activity_controls = None
        self.correspondence_controls = None
        self.document_controls = None
        self.device_controls = None
        self.localization_controls = None
        self.task_controls = None
        self.task_details = None
        self.tasks_manager = None
        self.property_document_manager = None
        self.regulation_manager = None
        self.invoice_manager = None
        self.activity_manager = None
        self.correspondence_manager = None
        self.document_manager = None
        self.localization_manager = None
        self.device_manager = None
        self.dict_manager = None
        self.dict_manager = None
        self.template_manager = None
        self.email_template_manager = None
        self.addressee_manager = None
        self.project_manager = None
        self.todo_mapper = None
        self.report_editor = None
        self.batch_report_editor = None
        self.todo_editor = None
        self.settingInspector = None

        self.action_doc_templates.triggered.connect(self.doc_templates_manager)  # documents_templates
        self.action_mail_templates.triggered.connect(self.mail_templates_manager)  # email_templates
        self.action_setting.triggered.connect(self.settings_inspector)
        self.action_engineers.triggered.connect(self.on_project_manager)
        self.actionEdytor.triggered.connect(self.on_report_editor)
        self.actionBatchProcessing.triggered.connect(self.on_batch_processing_report_editor)
        self.actionNotebook.triggered.connect(self.open_notebook)
        self.actionToDo.triggered.connect(self.on_todo_action)
        self.actionListToDo.triggered.connect(self.on_todo_list_action)
        self.actionProjectLabel.triggered.connect(self.on_project_label_action)

        self.install_filters()
        self.init_managers(self.dbase)
        self.init_controls()
        self.tabs_case_segments.setStyleSheet(styles.QTabBar_qss)
        self.action_documentation_label.triggered.connect(self.document_controls.print_docs_label)

    def init_controls(self):
        device_controls = [self.btn_devices_add, self.btn_devices_edit, self.btn_devices_delete]
        self.device_controls = DeviceControls.DeviceControl(device_controls, self.device_manager)

        localization_controls = [self.btn_localization_add, self.btn_localization_edit, self.btn_localization_delete,
                                 self.actionLokalizacja, self.device_controls]
        self.localization_controls = LocalizationControls.LocalizationControl(localization_controls, self.localization_manager)

        task_controls = [self.btn_task_add, self.btn_task_edit, self.btn_task_delete, self.btn_task_print, self.btn_task_clipboard,
                         self.actionZadanie]
        self.tasks_manager.task_controls = task_controls
        self.task_controls = TaskControls.TaskControl(self.tasks_manager, [self.localization_controls, self.device_controls])

        document_controls = [self.btn_document_add, self.btn_document_edit, self.btn_document_delete, self.btn_document_print,
                             self.btn_documentation_label, self.actionDokumentacja, self.actionEtykieta_pliku_dokumentu]
        self.document_controls = DocumentControls.DocumentControl(document_controls, self.document_manager)

        correspondence_controls = [self.btn_correspondence_add, self.btn_correspondence_edit, self.btn_correspondence_delete,
                                   self.btn_correspondence_print, self.actionKorespondencja, self.actionEtykieta_pliku_korespondencji]
        self.correspondence_controls = CorrespondenceControls.CorrespondenceControl(correspondence_controls, self.correspondence_manager)

        activity_controls = [self.btn_activity_add, self.btn_activity_edit, self.btn_activity_delete, self.btn_activity_print,
                             self.actionCzynno]
        self.activity_controls = ActivityControls.ActivityControl(activity_controls, self.activity_manager)

        invoice_controls = [self.btn_invoices_add, self.btn_invoices_edit, self.btn_invoices_delete, self.btn_invoices_print,
                            self.actionOp_ata, self.actionEtykieta_pliku_op_aty]
        self.invoice_controls = InvoiceControls.InvoiceControl(invoice_controls, self.invoice_manager)

        regulation_controls = [self.btn_deed_add, self.btn_deed_edit, self.btn_deed_delete, self.btn_deed_print, self.action_deal]
        self.regulation_controls = RegulationControls.RegulationControl(regulation_controls, self.regulation_manager)

        property_document_controls = [self.btn_asset_add, self.btn_asset_edit, self.btn_asset_delete, self.btn_asset_print,
                                      self.action_assets]
        self.regulation_document_controls = PropertyDocumentControls.PropertyDocumentControl(property_document_controls,
                                                                                             self.property_document_manager)

    def init_managers(self, dbase):
        self.task_details = TaskDetailsManager.TaskDetailsManager(self.txtbwr_task_details, self.txtbwr_task_info)
        related_task_controls = [self.task_details,
                                 self.spbx_search,
                                 self.lbl_info,
                                 self.btn_next,
                                 self.btn_previous,
                                 self.cbo_search_table,
                                 self.cbo_search_column,
                                 self.txt_search_value,
                                 self.btn_search,
                                 self.tabs_case_segments,
                                 self.cbo_search_sql_operators,
                                 self.btn_reset,
                                 self.btn_work_folder,
                                 self.menuAkcja,
                                 self.menu_reports,
                                 self.menuEtykiety,
                                 self.cbo_shortcuts,
                                 self.actionHTMLEditor,
                                 self.actionZadanie,
                                 self.actionParcel,
                                 self.actionSAP,
                                 self.actionOwner,
                                 self.actionDocSign,
                                 self.actionStreet,
                                 self.btn_last
                                 ]

        self.device_manager = DeviceManager.DeviceManager(self.tblvw_devices,
                                                          'tblDevices',
                                                          ColumnNames.device_table_column_titles,
                                                          self.statusBar, dbase)
        self.localization_manager = LocalizationManager.LocalizationManager(self.tblvw_localization,
                                                                            'tblLocalizations',
                                                                            ColumnNames.localization_table_column_titles,
                                                                            self.statusBar, dbase, self.device_manager)
        self.document_manager = DocumentManager.DocumentManager(self.tblvw_documents,
                                                                'tblKeyDocuments',
                                                                ColumnNames.document_table_column_titles,
                                                                self.statusBar, dbase)
        self.correspondence_manager = CorrespondenceManager.CorrespondenceManager(self.tblvw_correspondence,
                                                                                  'tblProjectCorrespondence',
                                                                                  ColumnNames.correspondence_table_column_titles,
                                                                                  self.statusBar, dbase)
        self.activity_manager = ActivityManager.ActivityManager(self.tblvw_activities,
                                                                'tblActions',
                                                                ColumnNames.activity_table_column_titles,
                                                                self.statusBar, dbase)
        self.invoice_manager = InvoiceManager.InvoiceManager(self.tblvw_invoices,
                                                             'tblInvoices',
                                                             ColumnNames.invoice_table_column_titles,
                                                             self.statusBar, dbase)
        self.regulation_manager = RegulationManager.RegulationManager(self.tblvw_deeds,
                                                                      'tblRegulations',
                                                                      ColumnNames.regulation_table_column_titles,
                                                                      self.statusBar, dbase)
        self.property_document_manager = PropertyDocumentManager.PropertyDocumentManager(self.tblvw_assets,
                                                                                         'tblPropertyDocuments',
                                                                                         ColumnNames.property_document_table_column_titles,
                                                                                         self.statusBar, dbase)

        related_task_tables = [self.localization_manager,
                               self.document_manager,
                               self.correspondence_manager,
                               self.activity_manager,
                               self.invoice_manager,
                               self.regulation_manager,
                               self.property_document_manager]
        self.tasks_manager = TaskManager.TaskManager(self.tblvw_tasks,
                                                     'tblProjects',
                                                     ColumnNames.task_table_column_titles,
                                                     self.statusBar,
                                                     dbase,
                                                     related_task_controls, related_task_tables)

        if self.todo_editor is None:
            self.todo_editor = ToDoItemsEditor.ToDoItemsEditor(self.tasks_manager)
        self.todo_editor.on_print()

        dict_actions = [self.action_activities,
                        self.action_devices,
                        self.action_documents,
                        self.action_tasks,
                        self.action_regulations,
                        self.action_places,
                        self.action_streets,
                        self.action_invoice,
                        self.actionPSPelements]

        if self.dict_manager is None:
            self.dict_manager = DictionaryManager.DictionaryManager(self.dbase, dict_actions)

        addressee_actions = [self.action_servisants, self.action_external, self.action_internal]
        self.addressee_manager = AddressBookManager.AddresseeManager(self.dbase, addressee_actions)

    def on_report_editor(self):
        self.report_editor = ReportsEditor.ReportsEditor(self.dbase, self.tasks_manager.settings)
        self.report_editor.show()

    def on_batch_processing_report_editor(self):
        self.batch_report_editor = BatchProcessingReportsEditor.BatchReportsEditor(self.dbase, self.tasks_manager)
        self.batch_report_editor.show()

    def on_todo_action(self):
        self.todo_mapper = ToDoMapper.ToDo(self.tasks_manager)
        self.todo_mapper.add_new_row()
        self.todo_mapper.set_current_data()
        self.todo_mapper.show()

    def on_todo_list_action(self):
        self.todo_editor.model.select()
        self.todo_editor.show()

    def open_notebook(self):
        path = self.tasks_manager.settings[0]
        programName = "notepad.exe"
        fileName = "notebook.txt"
        filePath = path + "\\" + fileName
        if os.path.isfile(filePath):
            sp.Popen([programName, filePath])
        else:
            info_boxes.informationBox('Informacja', f'Brak pliku: "{fileName}", w lokalizacji: "{path}"')

    def on_project_manager(self):
        if self.project_manager is None:
            self.project_manager = ProjectManager.ProjectManager(self.dbase, self.tasks_manager)
        self.project_manager.show()

    def on_project_label_action(self):
        templateInspector = TemplateInspector.TemplateInspector(self)
        htmlEditor = templateInspector.initHTML_editor(None, None, None)
        data = htmlEditor.gather_project_information()
        CaseNo = f'<div  style = "width: 100%; display: block;"><span style = "color: #a0008b; font-size: large; font-weight: bold;"> ({data[0]["Case"]}) </span><span style = "color: #264f70; font-size: large; font-weight: bold;"> {data[0]["SapNumber"]}</span></div>'
        Task = f'<span style = "color: #252d3a; font-size: medium; font-style: italic">{data[0]["Task"]}</span>'
        Caption = f'<h3 style = "text-align: center; margin-top: 25px; "><span>Zestawienie powierzchni eksploatacyjnej urządzeń na nieruchomości</span></h3>'
        table_content = CaseNo + Task + Caption
        project_label = DbData.project_label
        for localization in data[1]:
            table_content += f'<br>\n<table id = "{localization["ID"]}">\n'\
                   '\t<thead>\n'\
                   '\t\t<tr>\n'\
                   '\t\t\t<th>KW</th>\n'\
                   '\t\t\t<th>Nr dz.</th>\n'\
                   '\t\t\t<th>AM</th>\n'\
                   '\t\t\t<th>Obr.</th>\n'\
                   '\t\t</tr>\n'\
                   '\t</thead>\n'\
                   '\t<tbody>\n'\
                   '\t\t<tr>\n'\
                   f'\t\t\t<td><span style="background-color:rgb(255, 251, 0);padding: 3px;">{localization["LandRegister"]}</span></td>\n'\
                   f'\t\t\t<td style="text-align: center;">{localization["PlotNo"]}</td>\n'\
                   f'\t\t\t<td style="text-align: center;">{localization["MapNo"]}</td>\n'\
                   f'\t\t\t<td style="text-align: center;">{localization["Precinct"]}</td>\n'\
                   '\t\t</tr>'
            for device in data[2]:
               if localization["ID"] in device.keys():
                   for dev in device.values():
                       for d in dev:
                           table_content +='\t\t<tr>\n'\
                                f'\t\t\t<td colspan="4" style = "background-color: rgb(239, 242, 245);"><span style = "color: rgb(253, 0, 0); font-weight: bold;">&#10149;</span><b> {d["urządzenie"]}: </b> <span style = "color: rgb(37, 37, 170); margin-left: 15px;"><b>dł.:</b> {"{:.2f}".format(d["dł."])}m.</span>, <span style = "color: rgb(23, 87, 11);"><b>szer.:</b> {"{:.2f}".format(d["szer."])}m.</span>; <span style="margin-left: 15px;"><b>{"{:.2f}".format(float(d["dł."]) * float(d["szer."]))}m<sup>2</sup></b></span></td>\n'\
                                 '\t\t</tr>'
            table_content +='\t</tbody>\n'\
                  '</table>\n<br>'
        project_label = project_label.replace('[Content]',table_content)
        file_name = 'Zestawienie powierzchni eksploatacyjnej urządzeń.htm'
        path_repository = self.tasks_manager.settings[2] + '\\' + str(self.tasks_manager.current_parent_row)
        if not file_io.write_file(path_repository + '\\' + file_name, project_label):
            file_io.create_folder(path_repository)
            file_io.write_file(path_repository + '\\' + file_name, project_label)
        webbrowser.open(path_repository + '\\' + file_name)

    def doc_templates_manager(self):
        if self.template_manager is None:
            self.template_manager = TemplateManager.TemplateManager(self.dbase)
        self.template_manager.lstvw_templates.setCurrentIndex(self.template_manager.lstvw_templates.model().index(0, 0))
        self.template_manager.lstvw_templates.setFocus()
        self.template_manager.show()

    def mail_templates_manager(self):
        if self.email_template_manager is None:
            self.email_template_manager = MailTemplateManager.MailTemplateManager(self.dbase)
        self.email_template_manager.lstvw_templates.setCurrentIndex(self.email_template_manager.lstvw_templates.model().index(0, 0))
        self.email_template_manager.lstvw_templates.setFocus()
        self.email_template_manager.show()

    def settings_inspector(self):
        if self.settingInspector is None:
            self.settingInspector = SettingsInspector.SettingsInspector(self.tasks_manager.settings)
        self.settingInspector.show()

    def install_filters(self):
        self.spbx_search.installEventFilter(self)
        self.tblvw_localization.installEventFilter(self)
        self.tblvw_devices.installEventFilter(self)
        self.tblvw_documents.installEventFilter(self)
        self.tblvw_activities.installEventFilter(self)
        self.tblvw_assets.installEventFilter(self)
        self.tblvw_deeds.installEventFilter(self)
        self.tblvw_invoices.installEventFilter(self)
        self.tblvw_correspondence.installEventFilter(self)

    def closeEvent(self, event):
        backup_folder = self.tasks_manager.settings[19]
        if len(backup_folder) > 0:
            if file_io.create_folder(backup_folder):
                file_io.copy_file(os.path.expanduser("~") + '\\eRNI\\Base\\erni.db', backup_folder)
                info_boxes.informationBox("Zakończenie pracy", "Kopia danych została wykonana.")
        else:
            info_boxes.warningBox("Zakończenie pracy", "Kopia danych nie została wykonana.\n"
                                                       "Sprawdź, czy w ustawieniach aplikacji został wskazany folder kopii zapasowej.")

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if event.oldState() and Qt.WindowMinimized:
                qtRectangle = self.frameGeometry()
                centerPoint = QDesktopWidget().availableGeometry().center()
                qtRectangle.moveCenter(centerPoint)
                self.move(qtRectangle.topLeft())
                self.task_details.font_size = 12
                self.task_details.display_task_details()
            elif event.oldState() == Qt.WindowNoState or self.windowState() == Qt.WindowMaximized:
                self.task_details.font_size = 14
                self.task_details.display_task_details()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.FocusIn:
            if source is self.spbx_search:
                self.spbx_search.clear()
        if event.type() == QtCore.QEvent.FocusOut:
            if source is self.tblvw_localization or \
                    source is self.tblvw_devices or \
                    source is self.tblvw_documents or \
                    source is self.tblvw_correspondence or \
                    source is self.tblvw_deeds or \
                    source is self.tblvw_activities or \
                    source is self.tblvw_assets or \
                    source is self.tblvw_invoices:
                self.statusBar.clearMessage()
        return super(MainWindow, self).eventFilter(source, event)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    splash = SplashScreen()
    splash.lbl_progress.setVisible(False)
    splash.prb_progress.setVisible(False)

    splash.show()
    start = time.time()
    if splash.state:  # new database
        splash.lbl_progress.setVisible(True)
        splash.prb_progress.setVisible(True)
        while time.time() - start < 1.5:
            time.sleep(0.001)
            app.processEvents()
        splash.get_dictionary_data()

    else:
        while time.time() - start < 3:
            time.sleep(0.001)
            app.processEvents()
    splash.close()

    mainWindow = MainWindow(splash.db)
    mainWindow.tasks_manager.settings = file_io.read_encoded(basedir + '\\config.txt')

    if mainWindow.tasks_manager.settings is None:
        info_boxes.criticalBox('Błąd', 'Brak informacji konfiguracyjnych uniemożliwia dalszą pracę aplikacji')
        QMetaObject.invokeMethod(mainWindow, "close", Qt.QueuedConnection)
    else:
        PasswordControl(mainWindow)
        if len(mainWindow.tasks_manager.settings[18]) > 0:
            mainWindow.tasks_manager.load_shortcuts()
    app.exec_()


if __name__ == "__main__":
    main()