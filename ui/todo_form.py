# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todo_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(470, 392)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(470, 392))
        Form.setMaximumSize(QtCore.QSize(470, 392))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowFilePath("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.dte_registration_date = QtWidgets.QDateEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dte_registration_date.sizePolicy().hasHeightForWidth())
        self.dte_registration_date.setSizePolicy(sizePolicy)
        self.dte_registration_date.setDisplayFormat("yyyy.MM.dd")
        self.dte_registration_date.setCalendarPopup(True)
        self.dte_registration_date.setObjectName("dte_registration_date")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dte_registration_date)
        self.sbx_case = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbx_case.sizePolicy().hasHeightForWidth())
        self.sbx_case.setSizePolicy(sizePolicy)
        self.sbx_case.setMinimumSize(QtCore.QSize(150, 0))
        self.sbx_case.setSpecialValueText("")
        self.sbx_case.setSuffix("")
        self.sbx_case.setPrefix("")
        self.sbx_case.setMaximum(999999999)
        self.sbx_case.setObjectName("sbx_case")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbx_case)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_todo = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_todo.sizePolicy().hasHeightForWidth())
        self.txt_todo.setSizePolicy(sizePolicy)
        self.txt_todo.setMinimumSize(QtCore.QSize(0, 198))
        self.txt_todo.setTabChangesFocus(True)
        self.txt_todo.setObjectName("txt_todo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_todo)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dte_deadline = QtWidgets.QDateEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dte_deadline.sizePolicy().hasHeightForWidth())
        self.dte_deadline.setSizePolicy(sizePolicy)
        self.dte_deadline.setSpecialValueText("")
        self.dte_deadline.setProperty("showGroupSeparator", False)
        self.dte_deadline.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dte_deadline.setDisplayFormat("yyyy.MM.dd")
        self.dte_deadline.setCalendarPopup(True)
        self.dte_deadline.setObjectName("dte_deadline")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dte_deadline)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        self.btn_ok.setMinimumSize(QtCore.QSize(75, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btn_ok.setFont(font)
        self.btn_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ok.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_ok.setAutoFillBackground(False)
        self.btn_ok.setStyleSheet("QPushButton {\n"
"border: 1px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(spread:pad, x1:0.529318, y1:1, x2:0.511909, y2:0.262, stop:0.295455 rgba(192, 192, 192, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.507, y1:0.937, x2:0.489, y2:0.08, stop:0 rgba(207, 207, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
" }\n"
"QPushButton:pressed {\n"
" background-color: qlineargradient(spread:pad, x1:0.513, y1:0, x2:0.495, y2:0.886, stop:0.306818 rgba(208, 208, 208, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.btn_ok.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/icon/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon1)
        self.btn_ok.setIconSize(QtCore.QSize(32, 32))
        self.btn_ok.setAutoDefault(True)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.label.setBuddy(self.dte_registration_date)
        self.label_2.setBuddy(self.sbx_case)
        self.label_3.setBuddy(self.txt_todo)
        self.label_4.setBuddy(self.dte_deadline)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.dte_registration_date, self.sbx_case)
        Form.setTabOrder(self.sbx_case, self.txt_todo)
        Form.setTabOrder(self.txt_todo, self.dte_deadline)
        Form.setTabOrder(self.dte_deadline, self.btn_ok)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Do zrobienia"))
        self.label.setText(_translate("Form", "Data wpisu"))
        self.label_2.setText(_translate("Form", "Teczka"))
        self.label_3.setText(_translate("Form", "Do zrobienia"))
        self.label_4.setText(_translate("Form", "Termin"))
        self.btn_ok.setToolTip(_translate("Form", "Zapisz"))
import res.main_form_rc
