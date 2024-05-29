from PyQt5.QtWidgets import QDialog
from ui.settings_form import Ui_Form
from utils import file_io


class SettingsInspector(QDialog, Ui_Form):
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.on_submit)
        self.settings = settings
        self.set_data()

    def set_data(self):
        try:
            self.txt_templates.setText(self.settings[0])
            self.txt_email_templates.setText(self.settings[1])
            self.txt_repos.setText(self.settings[2])
            self.txt_reports.setText(self.settings[3])
            self.txt_user_name.setText(self.settings[4])
            self.txt_position.setText(self.settings[5])
            self.txt_division.setText(self.settings[6])
            self.txt_user_address.setText(self.settings[7])
            self.txt_user_phone.setText(self.settings[8])
            self.txt_user_email.setText(self.settings[9])
            self.txt_user_password.setText(self.settings[10])
            self.txt_corpo_name.setText(self.settings[11])
            self.txt_corpo_address.setText(self.settings[12])
            self.txt_nip.setText(self.settings[13])
            self.txt_regon.setText(self.settings[14])
            self.txt_krs.setText(self.settings[15])
            self.txt_capital.setText(self.settings[16])
            self.txt_outlook.setText(self.settings[17])
            self.txt_shortcuts.setText(self.settings[18])
            self.txt_backup.setText(self.settings[19])

        except:
            for ctl in self.children():
                if ctl.__class__.__name__ == 'QLineEdit':
                    if not ctl.text():
                        self.txt_templates.setText('')
            return

    def on_submit(self):
        paths = []
        user_info = []
        corporation_info = []
        application_info = []
        self.settings.clear()

        paths.append(self.txt_templates.text())
        paths.append(self.txt_email_templates.text())
        paths.append(self.txt_repos.text())
        paths.append(self.txt_reports.text())
        self.settings.append(paths)

        user_info.append(self.txt_user_name.text())
        user_info.append(self.txt_position.text())
        user_info.append(self.txt_division.text())
        user_info.append(self.txt_user_address.text())
        user_info.append(self.txt_user_phone.text())
        user_info.append(self.txt_user_email.text())
        user_info.append(self.txt_user_password.text())
        self.settings.append(user_info)

        corporation_info.append(self.txt_corpo_name.text())
        corporation_info.append(self.txt_corpo_address.text())
        corporation_info.append(self.txt_nip.text())
        corporation_info.append(self.txt_regon.text())
        corporation_info.append(self.txt_krs.text())
        corporation_info.append(self.txt_capital.text())
        self.settings.append(corporation_info)

        application_info.append(self.txt_outlook.text())
        application_info.append(self.txt_shortcuts.text())
        application_info.append(self.txt_backup.text())
        self.settings.append(application_info)

        with open(r'config.txt', 'w') as fp:
            for item in self.settings:
                for element in item:
                    data = file_io.base64_encode(element)
                    fp.write(data + '\n')
        self.close()