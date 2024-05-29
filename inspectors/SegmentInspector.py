from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QPushButton, QComboBox
import db.Query
from ui import segment_inspector


class SegmentInspector(QDialog, segment_inspector.Ui_SegmentInspector):
    def __init__(self, dbase, parent=None):
        super().__init__()
        self.parent = parent
        self.qtRectangle = None
        self.setupUi(self)
        self.dbase = dbase
        self.set_position()
        self.model = QStandardItemModel()
        self.lstvw_segments.setModel(self.model)
        self.lstvw_segments.doubleClicked.connect(self.choose_segment)
        self.load_content()

    def set_position(self):
        self.qtRectangle = self.parent.frameGeometry()
        x = self.parent.frameGeometry().width() + 3
        self.qtRectangle.translate(QPoint(x, 31))
        self.setGeometry(self.qtRectangle)

    def load_content(self):
        self.model.clear()
        result = db.Query.get_field_list('tblProjects', 'projectSegment', self.dbase, 'count')
        if not result: return
        result.sort()
        for i in result:
            self.model.appendRow(QStandardItem(self.convertTuple(i)))
        self.lstvw_segments.setFocus()

    def choose_segment(self):
        cbo_segment = self.parent.findChild(QComboBox, 'cbo_segment')
        cbo_segment.setCurrentIndex(self.lstvw_segments.currentIndex().row())
        self.close()

    @staticmethod
    def convertTuple(_tuple):
        _str = ' :: '.join(_tuple)
        return _str


    def closeEvent(self, event):
        btn = self.parent.findChild(QPushButton,"btn_check_segment")
        btn.show()
        self.parent.setFocus()