import json
import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAbstractItemView

import db.AssociatedFields
import db.ColumnNames
import db.Query
import utils.styles
from editors import HTMLEditor
from managers import TableManager
from utils import info_boxes, file_io


class TaskManager(TableManager.TableManager):
    def __init__(self, table, db_table_name, column_titles, statusBar, dbase, related_controls, related_tables):
        super().__init__(table, db_table_name, column_titles, statusBar, dbase)
        self.settings = None
        self.shortcuts = None
        self.html_editor = None
        self.task_details = related_controls[0]
        self.search_navigator = related_controls[1]

        self.info = related_controls[2]
        self.button_next = related_controls[3]
        self.button_previous = related_controls[4]
        self.cbo_search_table = related_controls[5]
        self.cbo_search_column = related_controls[6]
        self.txt_search_value = related_controls[7]
        self.btn_search = related_controls[8]
        self.tabs_case_segments = related_controls[9]
        self.cbo_search_sql_operators = related_controls[10]
        self.btn_reset = related_controls[11]
        self.btn_work_folder = related_controls[12]
        self.menuAkcja = related_controls[13]
        self.menu_reports = related_controls[14]
        self.menuEtykiety = related_controls[15]
        self.cbo_shortcuts = related_controls[16]
        self.actionHTMLEditor = related_controls[17]
        self.actionZadanie = related_controls[18]
        self.actionParcel = related_controls[19]
        self.actionSAP = related_controls[20]
        self.actionOwner = related_controls[21]
        self.actionDocSign = related_controls[22]
        self.actionStreet = related_controls[23]
        self.btn_last = related_controls[24]

        self.cbo_shortcuts.setVisible(False)
        self.task_controls = None
        self.cbo_search_controls_init()

        for i in range(len(related_tables)):
            related_tables[i].parent = self

        self.localization_manager = related_tables[0]
        self.document_manager = related_tables[1]
        self.correspondence_manager = related_tables[2]
        self.activity_manager = related_tables[3]
        self.invoice_manager = related_tables[4]
        self.regulation_manager = related_tables[5]
        self.property_document_manager = related_tables[6]

        self.localization_manager.device_manager.parent = self
        self.activity_manager.task_details_manager = self.task_details
        self.column_values = {}
        self.column_titles = column_titles
        self.project_Ids = []
        self.set_model()
        self.set_relation(4, "tblStatus", "StatusId", "statusName")
        self.set_relation(8, "tblProjectCategories", "projectCategoryID", "projectCategoryName")
        self.set_column_sort_desc(0)
        self.select_model()
        self.info.setText('Ilość: ' + str(self.row_count()))

        self.setup_view()
        self.set_column_hidden(1)
        self.set_column_hidden(8)
        self.set_column_hidden(9)
        self.set_column_hidden(11)
        self.set_column_hidden(12)
        self.set_column_hidden(13)

        self.set_column_aligned(0)
        self.set_column_aligned(3)
        self.set_column_aligned(7)
        self.set_column_aligned(10)

        self.change_columns_order(7, 3)
        self.change_columns_order(10, 7)
        self.set_columns_fit_to_content()
        self.set_table_header_names()

        self.tabs_case_segments.setStyleSheet(utils.styles.QTabBar_qss)

        # set slots and signals
        self.table.selectionModel().selectionChanged.connect(self.on_row_changed)
        self.table.clicked.connect(self.on_row_changed)
        self.search_navigator.lineEdit().returnPressed.connect(lambda: self.on_text_changed())
        self.button_next.clicked.connect(lambda: self.on_move_index('next'))
        self.button_previous.clicked.connect(lambda: self.on_move_index('previous'))
        self.cbo_search_sql_operators.currentTextChanged.connect(self.sql_operators_changed)
        self.cbo_search_table.currentTextChanged.connect(self.cbo_search_table_text_changed)
        self.cbo_search_table.currentIndexChanged.connect(self.cbo_search_table_index_changed)
        self.cbo_search_column.currentIndexChanged.connect(self.cbo_search_column_index_changed)
        self.btn_search.clicked.connect(self.btn_search_was_toggled)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.btn_work_folder.clicked.connect(self.btn_work_folder_clicked)
        self.btn_last.clicked.connect(self.on_last_clicked)
        self.actionHTMLEditor.triggered.connect(self.on_html_editor)

        self.actionParcel.triggered.connect(lambda: self.on_find('parcel'))
        self.actionSAP.triggered.connect(lambda: self.on_find('project'))
        self.actionOwner.triggered.connect(lambda: self.on_find('owner'))
        self.actionDocSign.triggered.connect(lambda: self.on_find('document'))
        self.actionStreet.triggered.connect(lambda: self.on_find('street'))
        self.history = []
        if self.model.rowCount() > 0:
            self.select_row()
            # self.history.append(self.model.data(self.model.index(0, 0)))
        else:
            self.disable_controls()
        self.table.clicked.connect(self.take_cell_value)
        self.table.setFocus()


    def on_find(self, what):
        self.btn_reset_clicked()
        self.cbo_search_sql_operators.setCurrentIndex(0)
        match what:
            case 'parcel':
                self.cbo_search_table.setCurrentText(db.AssociatedFields.table_titles['localization_table_column_titles'])
                self.cbo_search_column.setCurrentText(db.AssociatedFields.localization_table_column_titles[2])
                self.cbo_search_sql_operators.setCurrentIndex(4)
            case 'project':
                self.cbo_search_table.setCurrentText(db.AssociatedFields.table_titles['task_table_column_titles'])
                self.cbo_search_column.setCurrentText(db.AssociatedFields.task_table_column_titles[2])
            case 'owner':
                self.cbo_search_table.setCurrentText(db.AssociatedFields.table_titles['localization_table_column_titles'])
                self.cbo_search_column.setCurrentText(db.AssociatedFields.localization_table_column_titles[8])
            case 'document':
                self.cbo_search_table.setCurrentText(db.AssociatedFields.table_titles['document_table_column_titles'])
                self.cbo_search_column.setCurrentText(db.AssociatedFields.document_table_column_titles[1])
            case 'street':
                self.cbo_search_table.setCurrentText(db.AssociatedFields.table_titles['localization_table_column_titles'])
                self.cbo_search_column.setCurrentText(db.AssociatedFields.localization_table_column_titles[5])

        self.txt_search_value.setFocus()

    def disable_controls(self):
        self.set_search_controls(False)
        self.btn_search.setEnabled(False)
        self.info.setText("")
        self.tabs_case_segments.setEnabled(False)
        self.set_controls(False)

    def set_controls(self, isEnabled):
        self.button_next.setEnabled(isEnabled)
        self.button_previous.setEnabled(isEnabled)
        self.btn_work_folder.setEnabled(isEnabled)
        self.cbo_shortcuts.setEnabled(isEnabled)
        self.search_navigator.setEnabled(isEnabled)
        self.menuAkcja.setEnabled(isEnabled)
        self.menu_reports.setEnabled(isEnabled)
        self.menuEtykiety.setEnabled(isEnabled)
        self.table.setEnabled(isEnabled)

    def set_task_controls(self, isEnabled):
        for ctrl in self.task_controls:
            if ctrl.objectName() == 'btn_task_add': continue
            ctrl.setEnabled(isEnabled)

    def clear_check_controls(self):
        self.btn_search.setChecked(False)
        self.set_search_controls(True)
        self.cbo_search_column.clear()
        self.cbo_search_table.clear()
        self.cbo_search_sql_operators.clear()
        self.txt_search_value.clear()
        self.cbo_search_controls_init()
        self.project_Ids.clear()

    def btn_search_was_toggled(self, checked):
        if not checked:
            self.filter_off()
            self.txt_search_value.clear()
            self.project_Ids.clear()
            self.txt_search_value.setFocus()
        else:
            val = self.txt_search_value.text()
            db_operator = self.cbo_search_sql_operators.currentText()
            self.btn_last.setEnabled(False)

            if len(val) > 0 and len(self.cbo_search_column.currentText()) > 0 and len(db_operator) > 0:
                db_tbl = db.AssociatedFields.get_table_db_name(self.cbo_search_table.currentText())
                col = self.cbo_search_column.currentText()
                tbl_titles = db.AssociatedFields.get_table_titles(self.cbo_search_table.currentText())
                col_titles = db.ColumnNames.get_db_column_titles(tbl_titles)
                db_col = db.ColumnNames.get_db_column_name(col_titles, col)

                if type(self.isTableRelated(db_col)) is tuple:
                    t = self.isTableRelated(db_col)
                    _id = db.Query.get_related_field_value(t[1], t[0], db_col, val, self.dbase)
                    if not _id:
                        info_boxes.informationBox("Brak danych",
                                                  "Nie odnaleziono danych spełniajacych zadane kryterium wyszukiwania")
                        self.cbo_search_table_index_changed()
                        return
                    else:
                        if len(_id) > 1:
                            info_boxes.criticalBox("Operator " + db_operator + " wywołał niejednoznaczność kryterium wyszukiwania.",
                                                   "W tabeli relacyjnej przeszukiwanego pola\n"
                                                   "odnaleziono więcej niż jedną pozycję \n"
                                                   "spełniającą zadane kryterium porównawcze.\n\n"
                                                   "Należy zawęzić kryteria wyszukiwania poprzez zmianę operatora lub doprecyzowanie wzorca.")
                            self.btn_reset_clicked()
                            return

                    val = _id[0]  # zamienia wartość przypisaną na wartość pola id z tabeli relacyjnej

                self.project_Ids = db.Query.get_projectID(db_tbl, db_col, db_operator, val, self.dbase)
                if not self.project_Ids:
                    self.project_Ids = []
                    info_boxes.informationBox("Brak danych",
                                              "Nie odnaleziono danych spełniajacych zadane kryterium wyszukiwania")
                    self.cbo_search_table_index_changed()
                    self.btn_search.setChecked(False)
                    return

                else:
                    self.project_Ids = list(dict.fromkeys(self.project_Ids))
                    self.project_Ids.sort(reverse=True)
                    ids = tuple(self.project_Ids)
                    if len(ids) == 1:
                        ids = str(ids)
                        result = ids.replace(",", "")
                        filter_str = 'projectID IN {}'.format(result)
                    else:
                        filter_str = 'projectID IN {}'.format(ids)

                    self.model.setFilter(filter_str)
                    self.info.setText('Znalezionych zadań: ' + str(len(self.project_Ids)))
                    self.task_controls[0].setEnabled(False)  # disable 'add task' button
                    self.actionZadanie.setEnabled(False)  # disable 'add task' menu action

                    self.table.setFocus()
                    self.select_row()
            else:
                info_boxes.criticalBox("Brak informacji.", "Nie wszystkie wymagane pola zostały wypełnione.")
                self.btn_search.setChecked(False)

    def filter_off(self):
        self.task_controls[0].setEnabled(True)
        self.actionZadanie.setEnabled(True)
        self.model.setFilter('')
        self.select_model()
        self.info.setText('Ilość: ' + str(self.row_count()))
        self.table.setFocus()
        self.select_row()
        self.task_controls[0].setEnabled(True)
        self.actionZadanie.setEnabled(True)


    @staticmethod
    def isTableRelated(field):
        for k, v in db.AssociatedFields.relational_tables.items():
            if field == k:
                return v
        return False

    def set_search_controls(self, isEnabled):
        self.txt_search_value.setEnabled(isEnabled)
        self.cbo_search_table.setEnabled(isEnabled)
        self.cbo_search_column.setEnabled(isEnabled)
        self.cbo_search_sql_operators.setEnabled(isEnabled)
        self.btn_reset.setEnabled(isEnabled)
        self.btn_search.setEnabled(isEnabled)

    def cbo_search_table_index_changed(self):
        self.txt_search_value.clear()

    def cbo_search_column_index_changed(self):
        self.txt_search_value.clear()

    def on_row_changed(self):
        try:
            for item in range(len(self.column_titles)):
                idx = self.model.index(self.current_row(), item)
                value = self.model.data(idx)
                header = self.model.headerData(item, Qt.Horizontal, Qt.DisplayRole)
                if value == '':
                    self.column_values[header] = '-'
                else:
                    self.column_values[header] = value
            caseNo = int(self.column_values['Teczka'])
            self.search_navigator.setValue(caseNo)
            self.current_parent_row = int(self.column_values['Teczka'])
            self.task_details.column_values = self.column_values
            self.task_details.display_task_details()
            self.cbo_shortcuts.setCurrentIndex(0)
            _filter = 'projectID = "{}"'

            self.set_tab_enabled(0, self.localization_manager, _filter)
            self.set_tab_enabled(1, self.document_manager, _filter)
            self.set_tab_enabled(2, self.correspondence_manager, _filter)
            self.set_tab_enabled(3, self.activity_manager, _filter)
            self.set_tab_enabled(4, self.invoice_manager, _filter)
            self.set_tab_enabled(5, self.regulation_manager, _filter)
            self.set_tab_enabled(6, self.property_document_manager, _filter)
            self.manage_history(caseNo)
            if self.model.rowCount() > 1:
                self.btn_last.setEnabled(True)
            else:
                self.btn_last.setEnabled(False)


        except:
            return

    def set_tab_enabled(self, index, manager, _filter):
        manager.current_parent_row = int(self.column_values['Teczka'])
        if not manager.change_filter(_filter):
            if manager.__class__.__name__ == 'LocalizationManager':
                manager.on_row_absence()
            self.tabs_case_segments.setTabEnabled(index, False)
        else:
            self.tabs_case_segments.setTabEnabled(index, True)

    def on_move_index(self, direction):
        if direction == 'next':
            self.select_row(self.current_row() + 1)
        else:
            self.select_row(self.current_row() - 1)
        self.manage_history(self.search_navigator.value())
        self.table.setFocus()

    def manage_history(self, item):
        try:
            if len(self.history) < 2:
                self.history.append(item)
            else:
                if not self.btn_last.isEnabled(): self.btn_last.setEnabled(True)
                for i in range(len(self.history)-1):
                    if self.history[i+1] == item:
                        return
                    self.history[i] = self.history[i+1]
                self.history.pop(1)
                self.history.append(item)
        except:
            return

    def on_last_clicked(self):
        self.search_navigator.setValue(self.history[0])
        self.on_text_changed()

    # def on_value_changed(self, value):
    #     for i in range(self.model.rowCount()):
    #         val = self.model.data(self.model.index(i, 0))
    #         if int(value) == val:
    #             index = self.model.index(i, 0)
    #             self.select_row(index.row())

    def on_text_changed(self):
        rc = self.model.rowCount()
        current = self.search_navigator.value()
        for i in range(rc):
            val = self.model.data(self.model.index(i, 0))
            if int(current) == val:
                index = self.model.index(i, 0)
                # index = self.model.index(self.current_row(), 0)
                self.table.scrollTo(index, QAbstractItemView.PositionAtCenter)
                self.select_row(index.row())
                self.table.setFocus()


    def cbo_search_controls_init(self):
        tables = []
        for k, v in db.AssociatedFields.table_titles.items():
            tables.append(db.AssociatedFields.table_titles[k])
        self.cbo_search_table.addItems(tables)
        self.cbo_search_sql_operators.addItems(db.Query.operators)
        self.cbo_search_sql_operators.setCurrentIndex(-1)

    def cbo_search_table_text_changed(self, s):
        self.cbo_search_column.clear()
        for k, v in db.AssociatedFields.table_titles.items():
            if db.AssociatedFields.table_titles[k] == s:
                current_table_column_titles = db.AssociatedFields.get_column_titles(k)
                self.cbo_search_column.addItems(current_table_column_titles)

    def sql_operators_changed(self, operator):
        placeholder_text = ''

        match operator:
            case '*.*':
                placeholder_text = 'zawiera...'
            case '*!*':
                placeholder_text = 'nie zawiera...'
            case '..*':
                placeholder_text = 'zaczyna się od...'
            case '*..':
                placeholder_text = 'kończy się na...'
            case '==':
                placeholder_text = 'równa się...'
            case '!=':
                placeholder_text = 'jest różne od...'
            case '>=':
                placeholder_text = 'jest większe lub równe...'
            case '<=':
                placeholder_text = 'jest mniejsze lub równe...'
            case '>':
                placeholder_text = 'jest większe od...'
            case '<':
                placeholder_text = 'jest mniejsze od...'

        self.txt_search_value.setPlaceholderText(placeholder_text)
        self.txt_search_value.setFocus()

    def btn_reset_clicked(self):
        self.cbo_search_table.setCurrentIndex(-1)
        self.cbo_search_table.setEnabled(True)
        self.cbo_search_column.setCurrentIndex(-1)
        self.cbo_search_column.setEnabled(True)
        self.cbo_search_sql_operators.setCurrentIndex(-1)
        self.cbo_search_sql_operators.setEnabled(True)
        self.btn_search.setChecked(False)
        self.filter_off()
        self.clear_check_controls()
        self.table.setFocus()

    def load_shortcuts(self):
        path = self.settings[18]
        if not path is None:
            result = file_io.read_file(path)
            if len(result) > 0:
                shortcuts = json.loads(result, strict=False)
                self.shortcuts = shortcuts
                for shortcut in shortcuts.items():
                    self.cbo_shortcuts.addItem(shortcut[0])
                    self.cbo_shortcuts.setVisible(True)
        else:
            return

    def btn_work_folder_clicked(self):
        if len(self.settings[2]) == 0:
            info_boxes.criticalBox("Brak informacji.", "Brak ścieżki dostępu w ustawieniach aplikacji.")
            return

        if not self.shortcuts is None:
            alias = self.cbo_shortcuts.currentText()

            if alias == 'Protokoły z Gminą W-w' or alias == 'PMIR':
                idx = self.model.index(self.current_row(), 2) # current index of SAPNo cell in the table
                value = self.model.data(idx)[5:]
                clipboard = QApplication.clipboard()
                clipboard.setText(value) # put into clipboard

            path = self.shortcuts[alias]
            if path.startswith('https://'):
                webbrowser.open(path)
            elif len(path) == 0:  # alias is empty
                file_io.open_folder(self.settings[2] + '\\' + str(self.current_parent_row), True)
            else:
                if not file_io.open_folder(path):
                    info_boxes.criticalBox("Brak lokalizacji.",
                                           "Brak określonej lokalizacji w ustawionej ścieżce dostępu.")
                    return

        else:
            file_io.open_folder(self.settings[2] + '\\' + str(self.current_parent_row), True)

    def take_cell_value(self, index):
        clipboard = QApplication.clipboard()
        for item in range(len(self.column_titles)):
            if item == index.column():
                header = self.model.headerData(item, Qt.Horizontal, Qt.DisplayRole)
                if header == "Teczka":
                    clipboard.setText(self.settings[2] + '\\' + str(index.data()))
                if header == "Nr SAP" or header == "Inżynier":
                    clipboard.setText(index.data())

    def on_html_editor(self):
        self.html_editor = HTMLEditor.HTMLEditor(None, None, self.settings[2] + '\\' + str(self.current_parent_row), self)
        self.html_editor.show()