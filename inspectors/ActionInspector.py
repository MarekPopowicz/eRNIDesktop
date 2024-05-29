from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QPushButton, QPlainTextEdit
from db import Query
from ui.action_inspector import Ui_Form


class ActionInspector(QDialog, Ui_Form):
    def __init__(self, dbase,  parent=None):
        super().__init__()
        self.dbase = dbase
        self.parent = parent
        self.qtRectangle = None
        self.setupUi(self)
        self.setWindowTitle("Czynności")
        self.set_position()
        self.model = QStandardItemModel()
        self.lstvw_actions.setModel(self.model)

        result = Query.get_field_list('tblActivityCategories', 'ActivityName', self.dbase)
        result.sort()
        for i in result:
            self.model.appendRow(QStandardItem(i))
        self.lstvw_actions.setCurrentIndex(self.model.index(0, 0))
        self.lstvw_actions.setFocus()
        self.lstvw_actions.doubleClicked.connect(self.choose_action)

    def set_position(self):
        self.qtRectangle = self.parent.frameGeometry()
        x = self.parent.frameGeometry().width()+3
        self.qtRectangle.translate(QPoint(x, 31))
        self.setGeometry(self.qtRectangle)

    def choose_action(self):
        txt_activity = self.parent.findChild(QPlainTextEdit, 'txt_activity_description')
        txt = txt_activity.toPlainText()
        if len(txt)>0:
            txt_activity.setPlainText(f'{txt} {self.lstvw_actions.currentIndex().data()}')
        else:
            txt_activity.setPlainText(self.lstvw_actions.currentIndex().data())


    def closeEvent(self, event):
        btn = self.parent.findChild(QPushButton, "btn_activity_inspector")
        btn.show()
        self.parent.setFocus()