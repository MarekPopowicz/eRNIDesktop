from controls import Controls
from mappers import PropertyDocumentMapper


class PropertyDocumentControl(Controls.Controls):
    def __init__(self, controls, table_manager):
        super().__init__(table_manager)
        self.btn_asset_add = controls[0]
        self.btn_asset_edit = controls[1]
        self.btn_asset_delete = controls[2]
        self.btn_asset_print = controls[3]
        self.action_assets = controls[4]

        self.mapper = PropertyDocumentMapper.PropertyDocumentMapper(self.manager, self)

        self.btn_asset_add.clicked.connect(self.add_asset_mapper)
        self.btn_asset_edit.clicked.connect(self.edit_asset_mapper)
        self.btn_asset_delete.clicked.connect(self.remove_pt_doc)
        self.btn_asset_print.clicked.connect(self.print_pt_docs)
        self.action_assets.triggered.connect(self.add_asset_mapper)

    def edit_asset_mapper(self):
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edit data
        self.mapper.show()
        self.enable_buttons(False)

    def add_asset_mapper(self):
        if self.manager.parent.model.rowCount() == 0:
            return
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(None)
        self.mapper.clear_data()
        self.mapper.show()
        self.enable_buttons(False)

    def print_pt_docs(self):
        caption_text = f'<span style = "color: #c71b38;">({self.get_project_data("projectID")})</span> <span>{self.get_project_data("projectSapNo")}</span><span style = "padding: 10px 10px"> Dokumenty majątkowe</span>'
        self.print('assets_report', caption_text, self.get_project_data("projectID"))

    def remove_pt_doc(self):
        result = self.remove_row()
        if result is None or result == -1 or result == True:
            return

        else:  # no more rows - disable controls
            self.manager.parent.tabs_case_segments.setTabEnabled(6, False)

    def enable_buttons(self, bool_value):
        self.btn_asset_add.setEnabled(bool_value)
        self.btn_asset_edit.setEnabled(bool_value)
        self.btn_asset_delete.setEnabled(bool_value)
        self.action_assets.setEnabled(bool_value)