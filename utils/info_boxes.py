from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox


def set_icon():
    icon = QIcon()
    icon.addPixmap(QPixmap("./res/icon/logo_small.png"), QIcon.Normal, QIcon.Off)
    return icon


def informationBox(title, text):
    icon = set_icon()
    informationMessageBox = QMessageBox()
    informationMessageBox.setWindowIcon(icon)
    informationMessageBox.setWindowTitle(title)
    informationMessageBox.setIcon(QMessageBox.Information)
    informationMessageBox.setText(text)
    informationMessageBox.exec()
    return


def criticalBox(title, text):
    icon = set_icon()
    criticalMessageBox = QMessageBox()
    criticalMessageBox.setWindowIcon(icon)
    criticalMessageBox.setWindowTitle(title)
    criticalMessageBox.setIcon(QMessageBox.Critical)
    criticalMessageBox.setText(text)
    criticalMessageBox.exec()
    return


def warningBox(title, text):
    icon = set_icon()
    warningMessageBox = QMessageBox()
    warningMessageBox.setWindowIcon(icon)
    warningMessageBox.setWindowTitle(title)
    warningMessageBox.setIcon(QMessageBox.Warning)
    warningMessageBox.setText(text)
    warningMessageBox.exec()
    return


def questionBox(title, text):
    icon = set_icon()
    warningMessageBox = QMessageBox()
    warningMessageBox.setWindowIcon(icon)
    warningMessageBox.setWindowTitle(title)
    warningMessageBox.setIcon(QMessageBox.Question)
    warningMessageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    warningMessageBox.setText(text)
    return warningMessageBox.exec()