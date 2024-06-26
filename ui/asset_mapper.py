# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asset_mapper.ui'
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
        Form.resize(450, 375)
        Form.setMinimumSize(QtCore.QSize(450, 375))
        Form.setMaximumSize(QtCore.QSize(450, 375))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/icon/assets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frm_header_frame = QtWidgets.QFrame(Form)
        self.frm_header_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frm_header_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frm_header_frame.setObjectName("frm_header_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frm_header_frame)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_projectId = QtWidgets.QLabel(self.frm_header_frame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_projectId.setFont(font)
        self.lbl_projectId.setStyleSheet("color: #F50A77")
        self.lbl_projectId.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_projectId.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_projectId.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_projectId.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbl_projectId.setObjectName("lbl_projectId")
        self.verticalLayout.addWidget(self.lbl_projectId)
        self.lbl_task_name = QtWidgets.QLabel(self.frm_header_frame)
        self.lbl_task_name.setMinimumSize(QtCore.QSize(0, 40))
        self.lbl_task_name.setMaximumSize(QtCore.QSize(16777215, 16777213))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_task_name.setFont(font)
        self.lbl_task_name.setStyleSheet("color: #145479;\n"
"font-weight: bold")
        self.lbl_task_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_task_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_task_name.setWordWrap(True)
        self.lbl_task_name.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbl_task_name.setObjectName("lbl_task_name")
        self.verticalLayout.addWidget(self.lbl_task_name)
        self.verticalLayout_3.addWidget(self.frm_header_frame)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_type = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_type.setFont(font)
        self.lbl_type.setObjectName("lbl_type")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_type)
        self.lbl_date = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_date)
        self.lbl_SAP = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_SAP.setFont(font)
        self.lbl_SAP.setObjectName("lbl_SAP")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_SAP)
        self.lbl_info = QtWidgets.QLabel(self.frame)
        self.lbl_info.setObjectName("lbl_info")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_info)
        self.cbo_type = QtWidgets.QComboBox(self.frame)
        self.cbo_type.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cbo_type.setObjectName("cbo_type")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbo_type)
        self.dta_date = QtWidgets.QDateEdit(self.frame)
        self.dta_date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dta_date.setCalendarPopup(True)
        self.dta_date.setDate(QtCore.QDate(1900, 1, 1))
        self.dta_date.setObjectName("dta_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dta_date)
        self.txt_SAP = QtWidgets.QLineEdit(self.frame)
        self.txt_SAP.setObjectName("txt_SAP")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_SAP)
        self.txt_info = QtWidgets.QPlainTextEdit(self.frame)
        self.txt_info.setTabChangesFocus(True)
        self.txt_info.setObjectName("txt_info")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_info)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(self.frame_2)
        self.btn_ok.setMinimumSize(QtCore.QSize(100, 40))
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
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cbo_type, self.dta_date)
        Form.setTabOrder(self.dta_date, self.txt_SAP)
        Form.setTabOrder(self.txt_SAP, self.txt_info)
        Form.setTabOrder(self.txt_info, self.btn_ok)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dokument OT/PT"))
        self.lbl_projectId.setText(_translate("Form", "Numer Inwestycji"))
        self.lbl_task_name.setText(_translate("Form", "Nazwa zadania"))
        self.lbl_type.setText(_translate("Form", "Typ"))
        self.lbl_date.setText(_translate("Form", "Data"))
        self.lbl_SAP.setText(_translate("Form", "Nr SAP"))
        self.lbl_info.setText(_translate("Form", "Uwagi"))
        self.dta_date.setDisplayFormat(_translate("Form", "yyyy.MM.dd"))
        self.btn_ok.setToolTip(_translate("Form", "Zapisz"))
import res.main_form_rc
