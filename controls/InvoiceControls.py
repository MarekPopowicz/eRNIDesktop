from controls import Controls
from generators import InvoiceTagGenerator
from mappers import InvoiceMapper


class InvoiceControl(Controls.Controls):
    def __init__(self, controls, table_manager):
        super().__init__(table_manager)
        self.btn_invoices_add = controls[0]
        self.btn_invoices_edit = controls[1]
        self.btn_invoices_delete = controls[2]
        self.btn_invoices_print = controls[3]
        self.actionOp_ata = controls[4]
        self.actionEtykieta_pliku_op_aty = controls[5]

        self.mapper = InvoiceMapper.InvoiceMapper(self.manager, self)
        self.file_tag_generator = None
        self.btn_invoices_add.clicked.connect(self.add_invoice_mapper)
        self.btn_invoices_edit.clicked.connect(self.edit_invoice_mapper)
        self.btn_invoices_delete.clicked.connect(self.remove_invoice)
        self.btn_invoices_print.clicked.connect(self.print_invoices)
        self.actionOp_ata.triggered.connect(self.add_invoice_mapper)
        self.actionEtykieta_pliku_op_aty.triggered.connect(self.tag_generator)

    def edit_invoice_mapper(self):
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edited data
        self.mapper.show()
        self.enable_buttons(False)



    def add_invoice_mapper(self):
        if self.manager.parent.model.rowCount() == 0:
            return
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(None)
        self.mapper.set_date()
        self.mapper.clear_data()
        self.mapper.show()
        self.enable_buttons(False)

    def tag_generator(self):
        if self.file_tag_generator is None:
            self.file_tag_generator = InvoiceTagGenerator.InvoiceTagGenerator(self)
        else:
            self.file_tag_generator.doc_data = self.generate_file_tag()
            if self.file_tag_generator.doc_data is None:
                return
            self.file_tag_generator.set_document_data()
        self.file_tag_generator.show()

    def generate_file_tag(self):
        doc_data = []
        sap_no = self.manager.parent.model.data(self.manager.parent.model.index(self.manager.parent.current_row(),
                                                                                self.manager.parent.model.fieldIndex(
                                                                                    "projectSapNo")))
        if self.manager.model.rowCount() > 0:
            doc_data.append(sap_no)  # 0
            for item in range(self.manager.model.columnCount()):
                idx = self.manager.model.index(self.manager.current_row(), item)
                if item in (self.manager.model.fieldIndex("projectID"),  # 5
                            self.manager.model.fieldIndex("invoiceNo"),  # 4
                            self.manager.model.fieldIndex("invoiceIssueDate"),  # 3
                            self.manager.model.fieldIndex("invoiceTitle"),  # 3
                            self.manager.model.fieldIndex("invoiceSellerName")  # 2
                            ):
                    value = self.manager.model.data(idx)
                    doc_data.append(value)

            return doc_data

    def print_invoices(self):
        caption_text = f'<span style = "color: #c71b38;">({self.get_project_data("projectID")})</span> <span>{self.get_project_data("projectSapNo")}</span><span style = "padding: 10px 10px"> Faktury</span>'
        self.print('invoice_report', caption_text, self.get_project_data("projectID"))

    def remove_invoice(self):
        result = self.remove_row()
        if result is None or result == -1 or result == True:
            return

        else:  # no more rows - disable controls
            self.manager.parent.tabs_case_segments.setTabEnabled(4, False)

    def enable_buttons(self, bool_value):
        self.btn_invoices_add.setEnabled(bool_value)
        self.btn_invoices_edit.setEnabled(bool_value)
        self.btn_invoices_delete.setEnabled(bool_value)
        self.actionOp_ata.setEnabled(bool_value)