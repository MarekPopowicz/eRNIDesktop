from PyQt5 import QtCore, QtWidgets


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class FloatDelegate(QtWidgets.QStyledItemDelegate):
    def displayText(self, value, index):
        if isinstance(value, float):
            return  str("%.2f" % value).replace('.', ',')
        return super().displayText(value, index)