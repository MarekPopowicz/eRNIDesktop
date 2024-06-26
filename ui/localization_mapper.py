# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'localization_mapper.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(450, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(450, 680))
        Form.setMaximumSize(QtCore.QSize(450, 680))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/icon/location.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.verticalLayout_2.addWidget(self.frm_header_frame)
        self.frm_body_frame = QtWidgets.QFrame(Form)
        self.frm_body_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frm_body_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frm_body_frame.setObjectName("frm_body_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frm_body_frame)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(0, 3, 0, 3)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lbl_status = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_status.setStyleSheet("font-weight: bold")
        self.lbl_status.setObjectName("lbl_status")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_status)
        self.cbo_status = QtWidgets.QComboBox(self.frm_body_frame)
        self.cbo_status.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbo_status.setStyleSheet("")
        self.cbo_status.setCurrentText("")
        self.cbo_status.setObjectName("cbo_status")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbo_status)
        self.lbl_register = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_register.setStyleSheet("font-weight: bold")
        self.lbl_register.setObjectName("lbl_register")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_register)
        self.txt_register = QtWidgets.QLineEdit(self.frm_body_frame)
        self.txt_register.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txt_register.setObjectName("txt_register")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_register)
        self.lbl_parcel = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_parcel.setStyleSheet("font-weight: bold")
        self.lbl_parcel.setObjectName("lbl_parcel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_parcel)
        self.txt_parcel = QtWidgets.QLineEdit(self.frm_body_frame)
        self.txt_parcel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_parcel.setObjectName("txt_parcel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_parcel)
        self.lbl_map = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_map.setStyleSheet("font-weight: bold")
        self.lbl_map.setObjectName("lbl_map")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_map)
        self.spb_map = QtWidgets.QSpinBox(self.frm_body_frame)
        self.spb_map.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spb_map.setObjectName("spb_map")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spb_map)
        self.lbl_area = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_area.setStyleSheet("font-weight: bold")
        self.lbl_area.setObjectName("lbl_area")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_area)
        self.cbo_area = QtWidgets.QComboBox(self.frm_body_frame)
        self.cbo_area.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cbo_area.setEditable(True)
        self.cbo_area.setMaxVisibleItems(20)
        self.cbo_area.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cbo_area.setObjectName("cbo_area")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cbo_area)
        self.lbl_street = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_street.setObjectName("lbl_street")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_street)
        self.lbl_place = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_place.setStyleSheet("font-weight: bold")
        self.lbl_place.setObjectName("lbl_place")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_place)
        self.cbo_place = QtWidgets.QComboBox(self.frm_body_frame)
        self.cbo_place.setEnabled(True)
        self.cbo_place.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cbo_place.setEditable(True)
        self.cbo_place.setMaxVisibleItems(20)
        self.cbo_place.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cbo_place.setObjectName("cbo_place")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cbo_place)
        self.lbl_region = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_region.setStyleSheet("font-weight: bold")
        self.lbl_region.setObjectName("lbl_region")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lbl_region)
        self.cbo_region = QtWidgets.QComboBox(self.frm_body_frame)
        self.cbo_region.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbo_region.setObjectName("cbo_region")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.cbo_region)
        self.lbl_link = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_link.setObjectName("lbl_link")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lbl_link)
        self.txt_link = QtWidgets.QLineEdit(self.frm_body_frame)
        self.txt_link.setObjectName("txt_link")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.txt_link)
        self.lbl_owner = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_owner.setStyleSheet("font-weight: bold")
        self.lbl_owner.setObjectName("lbl_owner")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lbl_owner)
        self.txt_name = QtWidgets.QPlainTextEdit(self.frm_body_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_name.sizePolicy().hasHeightForWidth())
        self.txt_name.setSizePolicy(sizePolicy)
        self.txt_name.setMaximumSize(QtCore.QSize(16777215, 70))
        self.txt_name.setTabChangesFocus(True)
        self.txt_name.setObjectName("txt_name")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.txt_name)
        self.lbl_additional_info = QtWidgets.QLabel(self.frm_body_frame)
        self.lbl_additional_info.setObjectName("lbl_additional_info")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lbl_additional_info)
        self.txt_additional_info = QtWidgets.QPlainTextEdit(self.frm_body_frame)
        self.txt_additional_info.setTabChangesFocus(True)
        self.txt_additional_info.setObjectName("txt_additional_info")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.txt_additional_info)
        self.txt_street = QtWidgets.QLineEdit(self.frm_body_frame)
        self.txt_street.setObjectName("txt_street")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_street)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_2.addWidget(self.frm_body_frame)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_addressbook = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addressbook.sizePolicy().hasHeightForWidth())
        self.btn_addressbook.setSizePolicy(sizePolicy)
        self.btn_addressbook.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_addressbook.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_addressbook.setStyleSheet("QPushButton {\n"
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
        self.btn_addressbook.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon/addressbook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addressbook.setIcon(icon1)
        self.btn_addressbook.setIconSize(QtCore.QSize(32, 32))
        self.btn_addressbook.setAutoDefault(False)
        self.btn_addressbook.setObjectName("btn_addressbook")
        self.horizontalLayout.addWidget(self.btn_addressbook)
        self.btn_ok = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        self.btn_ok.setMinimumSize(QtCore.QSize(0, 40))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/icon/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon2)
        self.btn_ok.setIconSize(QtCore.QSize(32, 32))
        self.btn_ok.setAutoDefault(True)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.btn_restore = QtWidgets.QPushButton(self.frame)
        self.btn_restore.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_restore.sizePolicy().hasHeightForWidth())
        self.btn_restore.setSizePolicy(sizePolicy)
        self.btn_restore.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_restore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_restore.setStyleSheet("QPushButton {\n"
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
        self.btn_restore.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/res/icon/transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_restore.setIcon(icon3)
        self.btn_restore.setIconSize(QtCore.QSize(32, 32))
        self.btn_restore.setObjectName("btn_restore")
        self.horizontalLayout.addWidget(self.btn_restore)
        spacerItem = QtWidgets.QSpacerItem(239, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_owner_inspector = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_owner_inspector.sizePolicy().hasHeightForWidth())
        self.btn_owner_inspector.setSizePolicy(sizePolicy)
        self.btn_owner_inspector.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_owner_inspector.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_owner_inspector.setStyleSheet("QPushButton {\n"
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
        self.btn_owner_inspector.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/res/icon/person_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_owner_inspector.setIcon(icon4)
        self.btn_owner_inspector.setIconSize(QtCore.QSize(32, 32))
        self.btn_owner_inspector.setObjectName("btn_owner_inspector")
        self.horizontalLayout.addWidget(self.btn_owner_inspector)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cbo_status, self.txt_register)
        Form.setTabOrder(self.txt_register, self.txt_parcel)
        Form.setTabOrder(self.txt_parcel, self.spb_map)
        Form.setTabOrder(self.spb_map, self.cbo_area)
        Form.setTabOrder(self.cbo_area, self.txt_street)
        Form.setTabOrder(self.txt_street, self.cbo_place)
        Form.setTabOrder(self.cbo_place, self.cbo_region)
        Form.setTabOrder(self.cbo_region, self.txt_link)
        Form.setTabOrder(self.txt_link, self.txt_name)
        Form.setTabOrder(self.txt_name, self.txt_additional_info)
        Form.setTabOrder(self.txt_additional_info, self.btn_addressbook)
        Form.setTabOrder(self.btn_addressbook, self.btn_owner_inspector)
        Form.setTabOrder(self.btn_owner_inspector, self.btn_ok)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lokalizacja"))
        self.lbl_projectId.setText(_translate("Form", "Numer Inwestycji"))
        self.lbl_task_name.setText(_translate("Form", "Nazwa zadania"))
        self.lbl_status.setText(_translate("Form", "Status"))
        self.lbl_register.setText(_translate("Form", "KW"))
        self.lbl_parcel.setText(_translate("Form", "Działka"))
        self.lbl_map.setText(_translate("Form", "AM"))
        self.lbl_area.setText(_translate("Form", "Obręb"))
        self.lbl_street.setText(_translate("Form", "Ulica"))
        self.lbl_place.setText(_translate("Form", "Miejscowość"))
        self.lbl_region.setText(_translate("Form", "Region"))
        self.lbl_link.setText(_translate("Form", "Link"))
        self.lbl_owner.setText(_translate("Form", "Właściciel"))
        self.lbl_additional_info.setText(_translate("Form", "Uwagi"))
        self.btn_addressbook.setToolTip(_translate("Form", "Dodaj podmiot"))
        self.btn_ok.setToolTip(_translate("Form", "Zapisz"))
        self.btn_restore.setToolTip(_translate("Form", "Przywróć dane"))
        self.btn_owner_inspector.setToolTip(_translate("Form", "Wstaw dane o właścicielu"))
import res.main_form_rc
