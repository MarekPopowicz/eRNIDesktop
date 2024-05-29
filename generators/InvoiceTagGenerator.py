import ui.file_tag_generator
from PyQt5.QtWidgets import QDialog, QApplication
from utils import info_boxes

class InvoiceTagGenerator(QDialog, ui.file_tag_generator.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.doc_data = parent.generate_file_tag()
        self.btn_ok.clicked.connect(self.copy_to_clipboard)
        self.set_document_data()


    def set_document_data(self):
        self.cbx_extension.setChecked(True)
        if self.doc_data is None:
            info_boxes.criticalBox('Brak danych', 'Brak aktualnego wiersza danych uniemożliwia wykonanie operacji.')
            return

        self.lbl_caption.setText(f'({self.doc_data[5]}) | {self.doc_data[0]} | {self.doc_data[1]} | {self.doc_data[4]} | {self.doc_data[2]} | {self.doc_data[3]}')

        self.doc_data[2] = self.doc_data[2].replace('/', '_').strip()
        self.doc_data[2] = self.doc_data[2].replace('\\', '_').strip()
        # self.doc_data[4] = self.doc_data[4].replace(' ', '_').strip()
        # self.doc_data[3] = self.doc_data[3].replace(' ', '_').strip()

        doc_file_tag = f'({self.doc_data[5]}) {self.doc_data[0]} {self.doc_data[1]} {self.doc_data[4]} {self.doc_data[2]} {self.doc_data[3]}.pdf'
        self.lbl_lenght.setText(f'Długość: {len(doc_file_tag)-4} znaków')
        self.txt_file_tag.setText(doc_file_tag)



    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        if self.cbx_extension.isChecked():
            clipboard.setText(self.txt_file_tag.text())
        else:
            clipboard.setText(self.txt_file_tag.text()[:len(self.txt_file_tag.text())-4])

        self.close()

