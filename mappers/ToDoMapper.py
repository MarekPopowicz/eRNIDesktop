import ui.todo_form
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper
from utils import info_boxes
from PyQt5.QtCore import Qt, QDate, QModelIndex
from PyQt5.QtSql import QSqlTableModel


class ToDo(QDialog, ui.todo_form.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)  # destroy window object on close
        self.model = QSqlTableModel(db=parent.dbase)
        self.model.setTable("tblToDo")
        self.model.select()
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.addMapping(self.txt_todo, self.model.fieldIndex("todoItem"))
        self.mapper.addMapping(self.dte_registration_date, self.model.fieldIndex("todoRegistrationDate"))
        self.mapper.addMapping(self.sbx_case, self.model.fieldIndex("todoTaskCase"))
        self.mapper.addMapping(self.dte_deadline, self.model.fieldIndex("todoDeadLine"))
        self.btn_ok.clicked.connect(self.on_submit)
        self.txt_todo.setFocus()

    def set_current_data(self):
        self.dte_registration_date.setDate(QDate.currentDate())
        self.dte_deadline.setDate(QDate.currentDate().addDays(7))
        case = self.parent.model.data(self.parent.model.index(self.parent.current_row(), 0))
        self.sbx_case.setValue(case)

    def add_new_row(self):
        row = int(self.model.rowCount())  # finds which row is to add
        self.model.insertRow(row)  # creates new row
        index = QModelIndex(self.model.index(row, 0))
        self.mapper.setCurrentModelIndex(index)  # selects new row
        return row

    def edit_row(self, index):
        self.mapper.setCurrentIndex(index.row())


    def on_submit(self):
        if not self.txt_todo.toPlainText():
            info_boxes.informationBox("Brak wymaganych informacji",
                                      "Nie wszystkie wymagane pola zostały prawidłowo wypełnione.")
        else:
            if not self.mapper.submit():
                msg = self.model.lastError().text()
                if len(msg) > 0:
                    info_boxes.criticalBox("Błąd", msg)
                else:
                    info_boxes.criticalBox("Błąd", "Coś poszło nie tak.")
            else:
                if self.parent.__class__.__name__ == 'ToDoItemsEditor':
                    row = self.mapper.currentIndex()
                    self.parent.model.setSort(4, Qt.AscendingOrder)
                    self.parent.model.select()
                    self.parent.table.selectRow(row)
                    self.parent.table.setFocus()
            self.close()