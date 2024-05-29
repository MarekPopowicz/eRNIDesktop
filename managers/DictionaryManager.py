from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from db import Query
from ui.dictionary_form import Ui_Form
from utils import info_boxes


class DictionaryManager(QDialog, Ui_Form):
    def __init__(self, dbase, dictionary_actions):
        super().__init__()
        self.setupUi(self)
        self.db = dbase
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # destroy window object on close
        self.action_activities = dictionary_actions[0]
        self.action_devices = dictionary_actions[1]
        self.action_documents = dictionary_actions[2]
        self.action_tasks = dictionary_actions[3]
        self.action_regulations = dictionary_actions[4]
        self.action_places = dictionary_actions[5]
        self.action_streets = dictionary_actions[6]
        self.action_invoice = dictionary_actions[7]
        self.actionPSPelements = dictionary_actions[8]

        self.action_activities.triggered.connect(lambda: self.show_manager('tblActivityCategories'))  # activity
        self.action_devices.triggered.connect(lambda: self.show_manager('tblDeviceCategories'))  # device
        self.action_documents.triggered.connect(lambda: self.show_manager('tblKeyDocumentCategories'))  # document
        self.action_tasks.triggered.connect(lambda: self.show_manager('tblProjectTaskCategories'))  # task
        self.action_regulations.triggered.connect(lambda: self.show_manager('tblRegulationCategories'))  # regulation
        self.action_places.triggered.connect(lambda: self.show_manager('tblPlaces'))  # places
        self.action_streets.triggered.connect(lambda: self.show_manager('tblStreets'))  # streets
        self.action_invoice.triggered.connect(lambda: self.show_manager('tblInvoiceCategories'))  # invoice
        self.actionPSPelements.triggered.connect(lambda: self.show_manager('tblPSPelement'))  # PSP elements

        self.tblwgt_dictionary.clicked.connect(self.on_row_clicked)
        self.btn_search.clicked.connect(self.on_search_clicked)
        self.btn_add.clicked.connect(self.on_btn_add_clicked)
        self.btn_edit.clicked.connect(self.on_btn_edit_clicked)
        self.btn_ok.clicked.connect(self.on_btn_submit_clicked)
        self.btn_remove.clicked.connect(self.are_related_tables)

        self.tblwgt_dictionary.installEventFilter(self)

        self.table = ''
        self.column_name = ''
        self.column_id_name = ''

        self.related_table = ''
        self.current_id = 0

    def show_manager(self, dictionary):
        self.reset_controls()
        self.match_table(dictionary)
        self.show()

    def match_table(self, dictionary):
        self.table = dictionary
        match dictionary:
            case 'tblActivityCategories':
                self.lbl_dictionary_name.setText('Katalog czynności')
                self.lbl_element_value.setText('Czynność')
                self.column_name = 'ActivityName'
                self.related_table = ''
                self.column_id_name = 'ActivityCategoryID'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Czynność"])
            case 'tblDeviceCategories':
                self.lbl_dictionary_name.setText('Katalog urządzeń')
                self.lbl_element_value.setText('Urządzenie')
                self.column_name = 'deviceCategoryName'
                self.related_table = 'tblDevices'
                self.column_id_name = 'deviceCategoryID'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Urządzenie"])
            case 'tblKeyDocumentCategories':
                self.lbl_dictionary_name.setText('Katalog dokumentów')
                self.lbl_element_value.setText('Dokument')
                self.column_name = 'keyDocumentName'
                self.related_table = 'tblKeyDocuments'
                self.column_id_name = 'KeyDocumentCategoryID'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Dokument"])
            case 'tblProjectTaskCategories':
                self.lbl_dictionary_name.setText('Katalog zadań')
                self.lbl_element_value.setText('Zadanie')
                self.column_name = 'projectTaskName'
                self.related_table = ''
                self.column_id_name = 'projectTaskCategoryId'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Zadanie"])
            case 'tblRegulationCategories':
                self.lbl_dictionary_name.setText('Katalog regulacji')
                self.lbl_element_value.setText('Regulacja')
                self.column_name = 'regulationCategoryName'
                self.related_table = 'tblRegulations'
                self.column_id_name = 'regulationCategoryID'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Regulacja"])
            case 'tblPlaces':
                self.lbl_dictionary_name.setText('Katalog miejscowości')
                self.lbl_element_value.setText('Miejscowość')
                self.column_name = 'placeName'
                self.related_table = 'tblLocalizations'
                self.column_id_name = 'placeID'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Miejscowość"])
            case 'tblStreets':
                self.lbl_dictionary_name.setText('Katalog ulic')
                self.lbl_element_value.setText('Ulica')
                self.column_name = 'streetName'
                self.related_table = ''
                self.column_id_name = 'streetID'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Ulica"])
            case 'tblInvoiceCategories':
                self.lbl_dictionary_name.setText('Katalog opłat')
                self.lbl_element_value.setText('Opłata')
                self.column_name = 'invoiceTitle'
                self.related_table = 'tblInvoices'
                self.column_id_name = 'invoiceCategoryId'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Tytuł"])
            case 'tblPSPelement':
                self.lbl_dictionary_name.setText('Katalog elementów PSP')
                self.lbl_element_value.setText('Element')
                self.column_name = 'elementValue'
                self.related_table = ''
                self.column_id_name = 'elementId'
                self.tblwgt_dictionary.setHorizontalHeaderLabels(["Pozycja", "Element"])

        self.tblwgt_dictionary.setStyleSheet("""
             QTableWidget::item {padding-left: 5px; border: 0px;}
             QHeaderView::section {padding-left: 9px; padding-right: 9px; height: 30px;}
            """)

        self.load_data(f'SELECT * FROM {self.table}')

    def load_data(self, sql_query):
        rows = Query.get_data(self.db, sql_query, 2)
        if not rows:
            self.btn_edit.setEnabled(False)
            self.btn_remove.setEnabled(False)
            return False
        self.tblwgt_dictionary.setRowCount(len(rows))
        self.tblwgt_dictionary.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        for row in rows:
            inx = rows.index(row)
            self.tblwgt_dictionary.setItem(inx, 0, QTableWidgetItem(str(row[0])))
            self.tblwgt_dictionary.setItem(inx, 1, QTableWidgetItem(row[1]))

        self.set_font()
        self.tblwgt_dictionary.selectRow(0)
        self.btn_ok.setEnabled(False)
        self.current_id = self.tblwgt_dictionary.item(0, 0).text()
        self.txt_element.setPlainText(self.tblwgt_dictionary.item(0, 1).text())
        return True

    def on_search_clicked(self, checked):
        if checked:
            if len(self.txt_search.text()) > 0:
                result = self.load_data(f"SELECT * FROM {self.table} WHERE {self.column_name} LIKE '%{self.txt_search.text()}%'")
                if not result:
                    info_boxes.informationBox("Brak danych",
                                              "Operacja wyszukiwania nie zwrócila wyników zgodnych ze wskazanym wzorcem")
                    self.btn_search.setChecked(False)
                    self.txt_search.clear()
                    self.tblwgt_dictionary.setFocus()
                    return
            else:
                info_boxes.criticalBox("Odmowa wykonania operacji",
                                       "Należy podać dane do wyszukania.")
                self.btn_search.setChecked(False)
                self.tblwgt_dictionary.setFocus()
                return
        else:
            self.load_data(f'SELECT * FROM {self.table}')
            self.txt_search.clear()
            self.tblwgt_dictionary.setFocus()

    def set_font(self):
        fnt = QFont()
        fnt.setPointSize(10)
        fnt.setFamily("Tahoma")

        rowCount = self.tblwgt_dictionary.rowCount()
        columnCount = self.tblwgt_dictionary.columnCount()

        for i in range(rowCount):
            for j in range(columnCount):
                selectedItem = self.tblwgt_dictionary.item(i, j)
                selectedItem.setFont(fnt)

    def on_row_clicked(self):
        row = self.tblwgt_dictionary.currentRow()
        value = self.tblwgt_dictionary.item(row, 1).text()
        self.txt_element.setPlainText(value)
        self.current_id = self.tblwgt_dictionary.item(row, 0).text()
        self.reset_controls()

    def reset_controls(self):
        self.btn_remove.setEnabled(True)
        self.btn_edit.setEnabled(True)
        self.btn_add.setEnabled(True)
        self.txt_element.setReadOnly(True)
        self.btn_ok.setEnabled(False)
        self.txt_search.clear()
        self.btn_search.setChecked(False)
        self.tblwgt_dictionary.item(0, 0)
        self.tblwgt_dictionary.setFocus()

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            row = 0
            if source is self.tblwgt_dictionary and (event.key() == Qt.Key_Down):
                if self.tblwgt_dictionary.currentRow() < self.tblwgt_dictionary.rowCount() - 1:
                    row = self.tblwgt_dictionary.currentRow() + 1
            if source is self.tblwgt_dictionary and (event.key() == Qt.Key_Up):
                if self.tblwgt_dictionary.currentRow() > 0:
                    row = self.tblwgt_dictionary.currentRow() - 1
            value = self.tblwgt_dictionary.item(row, 1).text()
            self.current_id = self.tblwgt_dictionary.item(row, 0).text()
            self.txt_element.setPlainText(value)
        return super(DictionaryManager, self).eventFilter(source, event)

    def on_btn_add_clicked(self):
        self.btn_ok.setEnabled(True)
        self.txt_element.clear()
        self.btn_remove.setEnabled(False)
        self.btn_edit.setEnabled(False)
        self.txt_element.setReadOnly(False)
        self.txt_element.setFocus()
        self.btn_ok.operation = self.sender().objectName()

    def on_btn_edit_clicked(self):
        self.btn_ok.setEnabled(True)
        self.btn_remove.setEnabled(False)
        self.btn_add.setEnabled(False)
        self.txt_element.setReadOnly(False)
        self.txt_element.setFocus()
        self.btn_ok.operation = self.sender().objectName()

    def on_btn_submit_clicked(self):
        if self.btn_ok.operation == 'btn_add':
            self.add_record()
        else:
            self.edit_record()
        self.reset_controls()

    def add_record(self):
        row = self.tblwgt_dictionary.rowCount()
        if len(self.txt_element.toPlainText()) > 0:
            sql_command = f"INSERT INTO {self.table}({self.column_name}) VALUES('{self.txt_element.toPlainText()}')"
            if Query.add_value(self.db, sql_command):
                self.tblwgt_dictionary.insertRow(row)
                _id = Query.find_id_by_value(self.db, self.table, self.column_name,
                                             self.txt_element.toPlainText())  # find a new db auto incremented id
                self.tblwgt_dictionary.setItem(row, 0, QTableWidgetItem(str(_id)))  # insert a new id into the tbl widget
                self.tblwgt_dictionary.setItem(row, 1, QTableWidgetItem(self.txt_element.toPlainText()))
                self.tblwgt_dictionary.selectRow(row)
                self.current_id = self.tblwgt_dictionary.item(self.tblwgt_dictionary.currentRow(), 0).text()
                info_boxes.informationBox("Nowy element", "Operacja zapisu zakończona sukcesem.")
                self.tblwgt_dictionary.setFocus()
            else:
                info_boxes.criticalBox("Nowy element", "Operacja zapisu zakończyła się niepowodzeniem.")
                self.txt_element.clear()
                self.tblwgt_dictionary.setFocus()
        else:
            info_boxes.informationBox("Odmowa wykonania operacji", "Należy podać dane do zapisu.")
            self.txt_element.setFocus()

    def edit_record(self):
        if Query.update_value(self.db, self.table, self.column_name, self.txt_element.toPlainText(), self.column_id_name, self.current_id):
            self.tblwgt_dictionary.setItem(self.tblwgt_dictionary.currentRow(), 1,
                                           QTableWidgetItem(self.txt_element.toPlainText()))
            info_boxes.informationBox("Edycja elementu", "Operacja edycji zakończona sukcesem.")
        else:
            self.txt_element.setPlainText(self.tblwgt_dictionary.item(self.tblwgt_dictionary.currentRow(), 1).text())
            info_boxes.criticalBox("Edycja elementu", "Operacja edycji zakończyła się niepowodzeniem.")

        self.tblwgt_dictionary.setFocus()

    def are_related_tables(self):
        if self.related_table != '':
            result = Query.are_related_records(self.db, self.related_table, self.column_name,
                                               int(self.current_id))  # foreign key constraint
            if result > 0:
                info_boxes.criticalBox("Odmowa wykonania operacji", "Wybrana pozycja jest wykorzystana jako informacja w innej tabeli")
                self.tblwgt_dictionary.setFocus()
                return
            else:
                self.remove_data()
        else:
            self.remove_data()

    def remove_data(self):
        response = info_boxes.questionBox('Usunięcie danych',
                                          'Czy na pewno chcesz trwale usunąć bieżący wiersz ?')
        if response == 65536:
            self.tblwgt_dictionary.setFocus()
            return

        if Query.delete_records(self.db, self.table, self.column_id_name, self.current_id):
            self.tblwgt_dictionary.removeRow(self.tblwgt_dictionary.currentRow())
            self.txt_element.setPlainText(self.tblwgt_dictionary.item(self.tblwgt_dictionary.currentRow(), 1).text())
            info_boxes.informationBox("Usunięcie danych",
                                      "Wybrana pozycja została trwale usunięta")
        else:
            info_boxes.criticalBox("Usunięcie danych",
                                   "Wybrana pozycja nie została usunięta")
        self.tblwgt_dictionary.setFocus()

        if self.btn_search.isChecked():
            self.on_search_clicked(False)