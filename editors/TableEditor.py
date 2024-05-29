from PyQt5.QtWidgets import QDialog
import ui.table_wizard


class TableEditor(QDialog, ui.table_wizard.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_ok.clicked.connect(self.on_submit)


    def get_table_properties(self):
        table_properties = {
        'columns' : self.sbx_columns.value(),
        'rows' : self.sbx_rows.value(),
        'caption' : self.txt_tcaption.text(),
        'footer' : self.cbx_tfooter.isChecked(),
        'header' : self.cbx_theader.isChecked(),
        'border' : self.cbx_tborder.isChecked(),
        }
        return table_properties

    def reset_table_properties(self):
        self.sbx_columns.setValue(2)
        self.sbx_rows.setValue(1)
        self.txt_tcaption.setText('')
        self.cbx_tfooter.setChecked(False)
        self.cbx_theader.setChecked(False)
        self.cbx_tborder.setChecked(False)

    def on_submit(self):
        self.parent.table_properties = self.get_table_properties()
        self.close()
        self.parent.draw_table()