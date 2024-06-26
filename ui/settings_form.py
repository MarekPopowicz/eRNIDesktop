# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_form.ui'
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
        Form.resize(478, 784)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(478, 784))
        Form.setMaximumSize(QtCore.QSize(478, 784))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/icon/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lbl_templates = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_templates.setFont(font)
        self.lbl_templates.setObjectName("lbl_templates")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_templates)
        self.txt_templates = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_templates.sizePolicy().hasHeightForWidth())
        self.txt_templates.setSizePolicy(sizePolicy)
        self.txt_templates.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_templates.setFont(font)
        self.txt_templates.setObjectName("txt_templates")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_templates)
        self.lbl_email_templates = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_email_templates.setFont(font)
        self.lbl_email_templates.setObjectName("lbl_email_templates")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_email_templates)
        self.txt_email_templates = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_email_templates.sizePolicy().hasHeightForWidth())
        self.txt_email_templates.setSizePolicy(sizePolicy)
        self.txt_email_templates.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_email_templates.setFont(font)
        self.txt_email_templates.setObjectName("txt_email_templates")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_email_templates)
        self.lbl_repos = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_repos.setFont(font)
        self.lbl_repos.setObjectName("lbl_repos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_repos)
        self.txt_repos = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_repos.sizePolicy().hasHeightForWidth())
        self.txt_repos.setSizePolicy(sizePolicy)
        self.txt_repos.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_repos.setFont(font)
        self.txt_repos.setObjectName("txt_repos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_repos)
        self.lbl_reports = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_reports.setFont(font)
        self.lbl_reports.setObjectName("lbl_reports")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_reports)
        self.txt_reports = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_reports.sizePolicy().hasHeightForWidth())
        self.txt_reports.setSizePolicy(sizePolicy)
        self.txt_reports.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_reports.setFont(font)
        self.txt_reports.setObjectName("txt_reports")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_reports)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setContentsMargins(-1, 6, -1, 11)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(11)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl_user_name = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_user_name.setFont(font)
        self.lbl_user_name.setObjectName("lbl_user_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_user_name)
        self.txt_user_name = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_user_name.sizePolicy().hasHeightForWidth())
        self.txt_user_name.setSizePolicy(sizePolicy)
        self.txt_user_name.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user_name.setFont(font)
        self.txt_user_name.setObjectName("txt_user_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_user_name)
        self.lbl_position = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_position.setFont(font)
        self.lbl_position.setObjectName("lbl_position")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_position)
        self.txt_position = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_position.sizePolicy().hasHeightForWidth())
        self.txt_position.setSizePolicy(sizePolicy)
        self.txt_position.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_position.setFont(font)
        self.txt_position.setObjectName("txt_position")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_position)
        self.lbl_division = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_division.setFont(font)
        self.lbl_division.setObjectName("lbl_division")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_division)
        self.txt_division = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_division.sizePolicy().hasHeightForWidth())
        self.txt_division.setSizePolicy(sizePolicy)
        self.txt_division.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_division.setFont(font)
        self.txt_division.setObjectName("txt_division")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_division)
        self.lbl_user_address = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_user_address.setFont(font)
        self.lbl_user_address.setObjectName("lbl_user_address")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_user_address)
        self.txt_user_address = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_user_address.sizePolicy().hasHeightForWidth())
        self.txt_user_address.setSizePolicy(sizePolicy)
        self.txt_user_address.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user_address.setFont(font)
        self.txt_user_address.setObjectName("txt_user_address")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_user_address)
        self.lbl_user_phone = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_user_phone.setFont(font)
        self.lbl_user_phone.setObjectName("lbl_user_phone")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_user_phone)
        self.txt_user_phone = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_user_phone.sizePolicy().hasHeightForWidth())
        self.txt_user_phone.setSizePolicy(sizePolicy)
        self.txt_user_phone.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user_phone.setFont(font)
        self.txt_user_phone.setObjectName("txt_user_phone")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_user_phone)
        self.lbl_user_email = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_user_email.setFont(font)
        self.lbl_user_email.setObjectName("lbl_user_email")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_user_email)
        self.txt_user_email = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_user_email.sizePolicy().hasHeightForWidth())
        self.txt_user_email.setSizePolicy(sizePolicy)
        self.txt_user_email.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user_email.setFont(font)
        self.txt_user_email.setObjectName("txt_user_email")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_user_email)
        self.lbl_user_password = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_user_password.setFont(font)
        self.lbl_user_password.setObjectName("lbl_user_password")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_user_password)
        self.txt_user_password = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_user_password.sizePolicy().hasHeightForWidth())
        self.txt_user_password.setSizePolicy(sizePolicy)
        self.txt_user_password.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user_password.setFont(font)
        self.txt_user_password.setObjectName("txt_user_password")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txt_user_password)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lbl_corpo_name = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_corpo_name.setFont(font)
        self.lbl_corpo_name.setObjectName("lbl_corpo_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_corpo_name)
        self.txt_corpo_name = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_corpo_name.sizePolicy().hasHeightForWidth())
        self.txt_corpo_name.setSizePolicy(sizePolicy)
        self.txt_corpo_name.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_corpo_name.setFont(font)
        self.txt_corpo_name.setObjectName("txt_corpo_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_corpo_name)
        self.lbl_corpo_address = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_corpo_address.setFont(font)
        self.lbl_corpo_address.setObjectName("lbl_corpo_address")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_corpo_address)
        self.txt_corpo_address = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_corpo_address.sizePolicy().hasHeightForWidth())
        self.txt_corpo_address.setSizePolicy(sizePolicy)
        self.txt_corpo_address.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_corpo_address.setFont(font)
        self.txt_corpo_address.setObjectName("txt_corpo_address")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_corpo_address)
        self.lbl_nip = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_nip.setFont(font)
        self.lbl_nip.setObjectName("lbl_nip")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_nip)
        self.txt_nip = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nip.sizePolicy().hasHeightForWidth())
        self.txt_nip.setSizePolicy(sizePolicy)
        self.txt_nip.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_nip.setFont(font)
        self.txt_nip.setObjectName("txt_nip")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_nip)
        self.lbl_regon = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_regon.setFont(font)
        self.lbl_regon.setObjectName("lbl_regon")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_regon)
        self.txt_regon = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_regon.sizePolicy().hasHeightForWidth())
        self.txt_regon.setSizePolicy(sizePolicy)
        self.txt_regon.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_regon.setFont(font)
        self.txt_regon.setObjectName("txt_regon")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_regon)
        self.lbl_krs = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_krs.setFont(font)
        self.lbl_krs.setObjectName("lbl_krs")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_krs)
        self.txt_krs = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_krs.sizePolicy().hasHeightForWidth())
        self.txt_krs.setSizePolicy(sizePolicy)
        self.txt_krs.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_krs.setFont(font)
        self.txt_krs.setObjectName("txt_krs")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_krs)
        self.lbl_capital = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_capital.setFont(font)
        self.lbl_capital.setObjectName("lbl_capital")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_capital)
        self.txt_capital = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_capital.sizePolicy().hasHeightForWidth())
        self.txt_capital.setSizePolicy(sizePolicy)
        self.txt_capital.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_capital.setFont(font)
        self.txt_capital.setObjectName("txt_capital")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_capital)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout_2.setSpacing(26)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_outlook = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_outlook.setFont(font)
        self.lbl_outlook.setObjectName("lbl_outlook")
        self.horizontalLayout_2.addWidget(self.lbl_outlook)
        self.txt_outlook = QtWidgets.QLineEdit(Form)
        self.txt_outlook.setObjectName("txt_outlook")
        self.horizontalLayout_2.addWidget(self.txt_outlook)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout_3.setSpacing(32)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.txt_shortcuts = QtWidgets.QLineEdit(Form)
        self.txt_shortcuts.setObjectName("txt_shortcuts")
        self.horizontalLayout_3.addWidget(self.txt_shortcuts)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout_4.setSpacing(29)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.txt_backup = QtWidgets.QLineEdit(Form)
        self.txt_backup.setObjectName("txt_backup")
        self.horizontalLayout_4.addWidget(self.txt_backup)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(390, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(self.frame)
        self.btn_ok.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_ok.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btn_ok.setFont(font)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/icon/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon1)
        self.btn_ok.setIconSize(QtCore.QSize(32, 32))
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txt_templates, self.txt_email_templates)
        Form.setTabOrder(self.txt_email_templates, self.txt_repos)
        Form.setTabOrder(self.txt_repos, self.txt_reports)
        Form.setTabOrder(self.txt_reports, self.txt_user_name)
        Form.setTabOrder(self.txt_user_name, self.txt_position)
        Form.setTabOrder(self.txt_position, self.txt_division)
        Form.setTabOrder(self.txt_division, self.txt_user_address)
        Form.setTabOrder(self.txt_user_address, self.txt_user_phone)
        Form.setTabOrder(self.txt_user_phone, self.txt_user_email)
        Form.setTabOrder(self.txt_user_email, self.txt_user_password)
        Form.setTabOrder(self.txt_user_password, self.txt_corpo_name)
        Form.setTabOrder(self.txt_corpo_name, self.txt_corpo_address)
        Form.setTabOrder(self.txt_corpo_address, self.txt_nip)
        Form.setTabOrder(self.txt_nip, self.txt_regon)
        Form.setTabOrder(self.txt_regon, self.txt_krs)
        Form.setTabOrder(self.txt_krs, self.txt_capital)
        Form.setTabOrder(self.txt_capital, self.txt_outlook)
        Form.setTabOrder(self.txt_outlook, self.txt_shortcuts)
        Form.setTabOrder(self.txt_shortcuts, self.txt_backup)
        Form.setTabOrder(self.txt_backup, self.btn_ok)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ustawienia"))
        self.groupBox.setTitle(_translate("Form", "Ścieżki dostępu"))
        self.lbl_templates.setText(_translate("Form", "Szablony pism"))
        self.lbl_email_templates.setText(_translate("Form", "Szablony e-mail"))
        self.lbl_repos.setText(_translate("Form", "Repozytorium"))
        self.lbl_reports.setText(_translate("Form", "Raporty:"))
        self.groupBox_2.setTitle(_translate("Form", "Dane użytkownika"))
        self.lbl_user_name.setText(_translate("Form", "Imię i Nazwisko"))
        self.lbl_position.setText(_translate("Form", "Stanowisko"))
        self.lbl_division.setText(_translate("Form", "Wydział"))
        self.lbl_user_address.setText(_translate("Form", "Adres użytkownika"))
        self.lbl_user_phone.setText(_translate("Form", "Telefon"))
        self.lbl_user_email.setText(_translate("Form", "E-mail"))
        self.lbl_user_password.setText(_translate("Form", "Hasło"))
        self.groupBox_3.setTitle(_translate("Form", "Dane Spółki"))
        self.lbl_corpo_name.setText(_translate("Form", "Nazwa"))
        self.lbl_corpo_address.setText(_translate("Form", "Adres spółki"))
        self.lbl_nip.setText(_translate("Form", "NIP"))
        self.lbl_regon.setText(_translate("Form", "Regon"))
        self.lbl_krs.setText(_translate("Form", "KRS"))
        self.lbl_capital.setText(_translate("Form", "Kapitał"))
        self.lbl_outlook.setText(_translate("Form", "Outlook"))
        self.label.setText(_translate("Form", "Skróty"))
        self.label_2.setText(_translate("Form", "Backup"))
import res.main_form_rc
