# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addressee_manager.ui'
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
        Form.resize(900, 528)
        Form.setMinimumSize(QtCore.QSize(900, 528))
        Form.setMaximumSize(QtCore.QSize(900, 528))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/icon/logo_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_addressee = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_addressee.sizePolicy().hasHeightForWidth())
        self.lbl_addressee.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_addressee.setFont(font)
        self.lbl_addressee.setObjectName("lbl_addressee")
        self.horizontalLayout_4.addWidget(self.lbl_addressee)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.txt_search = QtWidgets.QLineEdit(self.frame)
        self.txt_search.setMinimumSize(QtCore.QSize(200, 25))
        self.txt_search.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"")
        self.txt_search.setClearButtonEnabled(True)
        self.txt_search.setObjectName("txt_search")
        self.horizontalLayout_4.addWidget(self.txt_search)
        self.btn_search = QtWidgets.QPushButton(self.frame)
        self.btn_search.setMaximumSize(QtCore.QSize(40, 35))
        self.btn_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/icon/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QtCore.QSize(25, 25))
        self.btn_search.setCheckable(True)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_4.addWidget(self.btn_search)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.lstvw_addressee = QtWidgets.QListWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstvw_addressee.sizePolicy().hasHeightForWidth())
        self.lstvw_addressee.setSizePolicy(sizePolicy)
        self.lstvw_addressee.setMinimumSize(QtCore.QSize(420, 0))
        self.lstvw_addressee.setFrameShape(QtWidgets.QFrame.Box)
        self.lstvw_addressee.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstvw_addressee.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lstvw_addressee.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.lstvw_addressee.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstvw_addressee.setAlternatingRowColors(True)
        self.lstvw_addressee.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstvw_addressee.setProperty("isWrapping", False)
        self.lstvw_addressee.setWordWrap(True)
        self.lstvw_addressee.setObjectName("lstvw_addressee")
        self.verticalLayout.addWidget(self.lstvw_addressee)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_add = QtWidgets.QPushButton(self.frame_4)
        self.btn_add.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_add.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add.setStyleSheet("QPushButton {\n"
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
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/icon/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon2)
        self.btn_add.setIconSize(QtCore.QSize(32, 32))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_edit = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy)
        self.btn_edit.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_edit.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_edit.setStyleSheet("QPushButton {\n"
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
        self.btn_edit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/res/icon/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit.setIcon(icon3)
        self.btn_edit.setIconSize(QtCore.QSize(32, 32))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.btn_remove = QtWidgets.QPushButton(self.frame_4)
        self.btn_remove.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_remove.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_remove.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_remove.setStyleSheet("QPushButton {\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/res/icon/decline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove.setIcon(icon4)
        self.btn_remove.setIconSize(QtCore.QSize(32, 32))
        self.btn_remove.setObjectName("btn_remove")
        self.horizontalLayout.addWidget(self.btn_remove)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.formLayout.setHorizontalSpacing(9)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.lbl_addresse_name = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_addresse_name.setFont(font)
        self.lbl_addresse_name.setText("Adresat")
        self.lbl_addresse_name.setObjectName("lbl_addresse_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_addresse_name)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setText("Ulica")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("Nr")
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setText("Lokal")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("Kod")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("Poczta")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setText("Telefon")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setText("Komórka")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setText("Email")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.cbo_addresse_street = QtWidgets.QComboBox(self.frame_2)
        self.cbo_addresse_street.setEnabled(True)
        self.cbo_addresse_street.setEditable(True)
        self.cbo_addresse_street.setMaxVisibleItems(20)
        self.cbo_addresse_street.setObjectName("cbo_addresse_street")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbo_addresse_street)
        self.cbo_addresse_post_office = QtWidgets.QComboBox(self.frame_2)
        self.cbo_addresse_post_office.setEditable(True)
        self.cbo_addresse_post_office.setMaxVisibleItems(20)
        self.cbo_addresse_post_office.setObjectName("cbo_addresse_post_office")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cbo_addresse_post_office)
        self.cbo_addresse_place = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo_addresse_place.sizePolicy().hasHeightForWidth())
        self.cbo_addresse_place.setSizePolicy(sizePolicy)
        self.cbo_addresse_place.setEditable(True)
        self.cbo_addresse_place.setMaxVisibleItems(20)
        self.cbo_addresse_place.setObjectName("cbo_addresse_place")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cbo_addresse_place)
        self.txt_addresse_name = QtWidgets.QPlainTextEdit(self.frame_2)
        self.txt_addresse_name.setMaximumSize(QtCore.QSize(16777215, 80))
        self.txt_addresse_name.setTabChangesFocus(True)
        self.txt_addresse_name.setReadOnly(False)
        self.txt_addresse_name.setObjectName("txt_addresse_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_addresse_name)
        self.txt_addresse_building = QtWidgets.QLineEdit(self.frame_2)
        self.txt_addresse_building.setEnabled(True)
        self.txt_addresse_building.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_addresse_building.setObjectName("txt_addresse_building")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_addresse_building)
        self.txt_addresse_apt = QtWidgets.QLineEdit(self.frame_2)
        self.txt_addresse_apt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_addresse_apt.setObjectName("txt_addresse_apt")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_addresse_apt)
        self.txt_addresse_zip_code = QtWidgets.QLineEdit(self.frame_2)
        self.txt_addresse_zip_code.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_addresse_zip_code.setObjectName("txt_addresse_zip_code")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_addresse_zip_code)
        self.txt_addresse_phone = QtWidgets.QLineEdit(self.frame_2)
        self.txt_addresse_phone.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txt_addresse_phone.setObjectName("txt_addresse_phone")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txt_addresse_phone)
        self.txt_addresse_mobile = QtWidgets.QLineEdit(self.frame_2)
        self.txt_addresse_mobile.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txt_addresse_mobile.setObjectName("txt_addresse_mobile")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.txt_addresse_mobile)
        self.txt_addresse_mail = QtWidgets.QLineEdit(self.frame_2)
        self.txt_addresse_mail.setObjectName("txt_addresse_mail")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.txt_addresse_mail)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("Miejscowość")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_ok = QtWidgets.QPushButton(self.frame_3)
        self.btn_ok.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_ok.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/res/icon/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon5)
        self.btn_ok.setIconSize(QtCore.QSize(32, 32))
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_2.addWidget(self.btn_ok)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.frame_2)

        self.retranslateUi(Form)
        self.lstvw_addressee.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lstvw_addressee, self.txt_search)
        Form.setTabOrder(self.txt_search, self.btn_search)
        Form.setTabOrder(self.btn_search, self.btn_add)
        Form.setTabOrder(self.btn_add, self.btn_edit)
        Form.setTabOrder(self.btn_edit, self.btn_remove)
        Form.setTabOrder(self.btn_remove, self.txt_addresse_name)
        Form.setTabOrder(self.txt_addresse_name, self.cbo_addresse_street)
        Form.setTabOrder(self.cbo_addresse_street, self.txt_addresse_building)
        Form.setTabOrder(self.txt_addresse_building, self.txt_addresse_apt)
        Form.setTabOrder(self.txt_addresse_apt, self.txt_addresse_zip_code)
        Form.setTabOrder(self.txt_addresse_zip_code, self.cbo_addresse_post_office)
        Form.setTabOrder(self.cbo_addresse_post_office, self.cbo_addresse_place)
        Form.setTabOrder(self.cbo_addresse_place, self.txt_addresse_phone)
        Form.setTabOrder(self.txt_addresse_phone, self.txt_addresse_mobile)
        Form.setTabOrder(self.txt_addresse_mobile, self.txt_addresse_mail)
        Form.setTabOrder(self.txt_addresse_mail, self.btn_ok)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Książka adresowa"))
        self.lbl_addressee.setText(_translate("Form", "Adresat"))
        self.lstvw_addressee.setSortingEnabled(False)
        self.btn_add.setToolTip(_translate("Form", "Dodaj szablon"))
        self.btn_edit.setToolTip(_translate("Form", "Edytuj szablon"))
        self.btn_remove.setToolTip(_translate("Form", "Usuń szablon"))
        self.btn_ok.setToolTip(_translate("Form", "Zapisz"))
import res.main_form_rc
