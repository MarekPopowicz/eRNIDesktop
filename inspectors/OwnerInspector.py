from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QPushButton, QPlainTextEdit
from db import Query
from ui import owner_inspector


class OwnerInspector(QDialog, owner_inspector.Ui_Form):
    def __init__(self, dbase, parent=None):
        super().__init__()
        self.parent = parent
        self.qtRectangle = None
        self.setupUi(self)
        self.dbase = dbase
        self.set_position()
        self.model = QStandardItemModel()
        self.lstvw_owners.setModel(self.model)
        self.lstvw_owners.doubleClicked.connect(self.choose_owner)
        self.load_data()

    def set_position(self):
        self.qtRectangle = self.parent.frameGeometry()
        x = self.parent.frameGeometry().width() + 3
        self.qtRectangle.translate(QPoint(x, 31))
        self.setGeometry(self.qtRectangle)

    def load_data(self):
        result = Query.get_field_list('tblExternalsAddressee', 'addresseeName', self.dbase)
        if not result: return
        self.model.clear()
        for i in result:
            self.model.appendRow(QStandardItem(i))
        result.sort()
        self.lstvw_owners.setCurrentIndex(self.model.index(0, 0))
        self.lstvw_owners.setFocus()


    def choose_owner(self):
        txt_owner = self.parent.findChild(QPlainTextEdit, 'txt_name')
        txt_owner.setPlainText(self.lstvw_owners.currentIndex().data())
        self.close()


    def closeEvent(self, event):
        btn = self.parent.findChild(QPushButton, "btn_owner_inspector")
        btn.show()
        self.parent.setFocus()