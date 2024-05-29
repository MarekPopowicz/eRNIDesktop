# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates_manager.ui'
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
        Form.resize(945, 530)
        Form.setMinimumSize(QtCore.QSize(945, 530))
        Form.setMaximumSize(QtCore.QSize(16777215, 530))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/icon/logo_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
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
        self.lbl_template = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_template.sizePolicy().hasHeightForWidth())
        self.lbl_template.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_template.setFont(font)
        self.lbl_template.setObjectName("lbl_template")
        self.verticalLayout.addWidget(self.lbl_template)
        self.lstvw_templates = QtWidgets.QListWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstvw_templates.sizePolicy().hasHeightForWidth())
        self.lstvw_templates.setSizePolicy(sizePolicy)
        self.lstvw_templates.setMinimumSize(QtCore.QSize(420, 0))
        self.lstvw_templates.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstvw_templates.setAlternatingRowColors(False)
        self.lstvw_templates.setObjectName("lstvw_templates")
        self.verticalLayout.addWidget(self.lstvw_templates)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_add = QtWidgets.QPushButton(self.frame_3)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/icon/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon1)
        self.btn_add.setIconSize(QtCore.QSize(32, 32))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_edit = QtWidgets.QPushButton(self.frame_3)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/icon/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit.setIcon(icon2)
        self.btn_edit.setIconSize(QtCore.QSize(32, 32))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.btn_remove = QtWidgets.QPushButton(self.frame_3)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/res/icon/decline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove.setIcon(icon3)
        self.btn_remove.setIconSize(QtCore.QSize(32, 32))
        self.btn_remove.setObjectName("btn_remove")
        self.horizontalLayout.addWidget(self.btn_remove)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setContentsMargins(6, 6, 6, 6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_template_name = QtWidgets.QLineEdit(self.frame_2)
        self.txt_template_name.setReadOnly(True)
        self.txt_template_name.setObjectName("txt_template_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_template_name)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_description = QtWidgets.QPlainTextEdit(self.frame_2)
        self.txt_description.setEnabled(True)
        self.txt_description.setTabChangesFocus(True)
        self.txt_description.setReadOnly(True)
        self.txt_description.setObjectName("txt_description")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_description)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txt_doc_service = QtWidgets.QPlainTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_doc_service.sizePolicy().hasHeightForWidth())
        self.txt_doc_service.setSizePolicy(sizePolicy)
        self.txt_doc_service.setMinimumSize(QtCore.QSize(0, 50))
        self.txt_doc_service.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txt_doc_service.setTabChangesFocus(True)
        self.txt_doc_service.setReadOnly(True)
        self.txt_doc_service.setPlainText("")
        self.txt_doc_service.setObjectName("txt_doc_service")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_doc_service)
        self.frm_checkboxes = QtWidgets.QFrame(self.frame_2)
        self.frm_checkboxes.setEnabled(False)
        self.frm_checkboxes.setFrameShape(QtWidgets.QFrame.Box)
        self.frm_checkboxes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_checkboxes.setObjectName("frm_checkboxes")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frm_checkboxes)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbx_documents = QtWidgets.QCheckBox(self.frm_checkboxes)
        self.cbx_documents.setEnabled(False)
        self.cbx_documents.setObjectName("cbx_documents")
        self.verticalLayout_2.addWidget(self.cbx_documents)
        self.cbx_lexical_forms = QtWidgets.QCheckBox(self.frm_checkboxes)
        self.cbx_lexical_forms.setObjectName("cbx_lexical_forms")
        self.verticalLayout_2.addWidget(self.cbx_lexical_forms)
        self.cbx_localization = QtWidgets.QCheckBox(self.frm_checkboxes)
        self.cbx_localization.setEnabled(False)
        self.cbx_localization.setObjectName("cbx_localization")
        self.verticalLayout_2.addWidget(self.cbx_localization)
        self.cbx_localization_KW = QtWidgets.QCheckBox(self.frm_checkboxes)
        self.cbx_localization_KW.setObjectName("cbx_localization_KW")
        self.verticalLayout_2.addWidget(self.cbx_localization_KW)
        self.cbx_are_attachements = QtWidgets.QCheckBox(self.frm_checkboxes)
        self.cbx_are_attachements.setEnabled(False)
        self.cbx_are_attachements.setObjectName("cbx_are_attachements")
        self.verticalLayout_2.addWidget(self.cbx_are_attachements)
        self.cbx_quantity_attachements = QtWidgets.QCheckBox(self.frm_checkboxes)
        self.cbx_quantity_attachements.setEnabled(False)
        self.cbx_quantity_attachements.setObjectName("cbx_quantity_attachements")
        self.verticalLayout_2.addWidget(self.cbx_quantity_attachements)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frm_checkboxes)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txt_info = QtWidgets.QPlainTextEdit(self.frame_2)
        self.txt_info.setTabChangesFocus(True)
        self.txt_info.setReadOnly(True)
        self.txt_info.setObjectName("txt_info")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_info)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(291, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_home_catalog = QtWidgets.QPushButton(self.frame_5)
        self.btn_home_catalog.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_home_catalog.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_home_catalog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home_catalog.setStyleSheet("QPushButton {\n"
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
        icon4.addPixmap(QtGui.QPixmap(":/icons/res/icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home_catalog.setIcon(icon4)
        self.btn_home_catalog.setIconSize(QtCore.QSize(32, 32))
        self.btn_home_catalog.setObjectName("btn_home_catalog")
        self.horizontalLayout_4.addWidget(self.btn_home_catalog)
        self.btn_ok = QtWidgets.QPushButton(self.frame_5)
        self.btn_ok.setEnabled(False)
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
        self.horizontalLayout_4.addWidget(self.btn_ok)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.frame_5)
        self.horizontalLayout_5.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Szablon Korespondencji Papierowej"))
        self.lbl_template.setText(_translate("Form", "Szablon"))
        self.btn_add.setToolTip(_translate("Form", "Dodaj szablon"))
        self.btn_edit.setToolTip(_translate("Form", "Edytuj szablon"))
        self.btn_remove.setToolTip(_translate("Form", "Usuń szablon"))
        self.label_2.setText(_translate("Form", "Nazwa"))
        self.label_3.setText(_translate("Form", "Opis"))
        self.label_4.setText(_translate("Form", "Przywołuje"))
        self.cbx_documents.setText(_translate("Form", "Wymaga wskazania dokumentu"))
        self.cbx_lexical_forms.setText(_translate("Form", "Włącz formy leksykalne nazwy dokumentu"))
        self.cbx_localization.setText(_translate("Form", "Wymaga wskazania lokalizacji"))
        self.cbx_localization_KW.setText(_translate("Form", "Lokalizacja z ujawnioną księgą wieczystą"))
        self.cbx_are_attachements.setText(_translate("Form", "Wymaga wskazania załączników"))
        self.cbx_quantity_attachements.setText(_translate("Form", "Wymaga wskazania liczby egz. załączników"))
        self.label_5.setText(_translate("Form", "Uwagi"))
        self.btn_home_catalog.setToolTip(_translate("Form", "Otwórz katalog domowy"))
        self.btn_ok.setToolTip(_translate("Form", "Zapisz ustawienia"))
import res.main_form_rc
