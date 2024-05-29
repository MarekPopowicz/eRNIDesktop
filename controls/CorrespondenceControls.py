from controls import Controls
from generators import CorrespondenceTagGenerator
from mappers import CorrespondenceMapper
from utils import info_boxes


class CorrespondenceControl(Controls.Controls):
    def __init__(self, controls, table_manager):
        super().__init__(table_manager)
        self.btn_correspondence_add = controls[0]
        self.btn_correspondence_edit = controls[1]
        self.btn_correspondence_delete = controls[2]
        self.btn_correspondence_print = controls[3]
        self.action_correspondence = controls[4]
        self.action_correspondence_file_tag = controls[5]

        self.mapper = CorrespondenceMapper.CorrespondenceMapper(self.manager, self)
        self.file_tag_generator = None

        self.btn_correspondence_edit.clicked.connect(self.edit_correspondence_mapper)
        self.btn_correspondence_add.clicked.connect(self.add_correspondence_mapper)
        self.btn_correspondence_delete.clicked.connect(self.remove_correspondence)
        self.btn_correspondence_print.clicked.connect(self.print_correspondence)
        self.action_correspondence.triggered.connect(self.add_correspondence_mapper)
        self.action_correspondence_file_tag.triggered.connect(self.tag_generator)

    def edit_correspondence_mapper(self):
        if self.manager.model.rowCount() == 0:
            return
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        idx = self.manager.table.currentIndex()
        self.mapper.set_index(idx)  # set current table index to edit data
        self.mapper.set_correspondence_direction()
        self.mapper.show()
        self.enable_buttons(False)


    def add_correspondence_mapper(self):
        if self.manager.parent.model.rowCount() == 0:
            return
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(None)
        self.mapper.set_correspondence_direction()
        self.mapper.show()
        self.enable_buttons(False)

    def tag_generator(self):
        if not self.generate_file_tag():
            info_boxes.criticalBox('Brak danych', 'Brak aktualnego wiersza danych uniemożliwia wykonanie operacji.')
            return

        if self.file_tag_generator is None:
            self.file_tag_generator = CorrespondenceTagGenerator.CorrespondenceTagGenerator(self)
        else:

            self.file_tag_generator.doc_data = self.generate_file_tag()
            if self.file_tag_generator.doc_data is None:
                return
            self.file_tag_generator.set_document_data()
        self.file_tag_generator.show()

    def generate_file_tag(self):
        doc_data = []
        sap_no = self.manager.parent.model.data(
            self.manager.parent.model.index(self.manager.parent.current_row(), self.manager.parent.model.fieldIndex("projectSapNo")))
        if self.manager.model.rowCount() > 0:
            doc_data.append(sap_no)  # 0
            for item in range(self.manager.model.columnCount()):
                idx = self.manager.model.index(self.manager.current_row(), item)
                if item in (self.manager.model.fieldIndex("projectID"),  # 5
                            self.manager.model.fieldIndex("projectCorrespondenceSign"),  # 4
                            self.manager.model.fieldIndex("projectCorrespondenceDate"),  # 3
                            self.manager.model.fieldIndex("projectCorrespondenceDirection"),  # 1
                            self.manager.model.fieldIndex("projectCorrespondenceSender")  # 2
                            ):
                    value = self.manager.model.data(idx)
                    doc_data.append(value)

            return doc_data
        else:
            return False

    def print_correspondence(self):
        caption_text = f'<span style = "color: #c71b38;">({self.get_project_data("projectID")})</span> <span>{self.get_project_data("projectSapNo")}</span><span style = "padding: 10px 10px"> Korespondencja</span>'
        self.print('correspondence_report', caption_text, self.get_project_data("projectID"))

    def remove_correspondence(self):
        result = self.remove_row()
        if result is None or result == -1 or result == True:
            return
        else:  # no more rows - disable controls
            self.manager.parent.tabs_case_segments.setTabEnabled(2, False)

    def enable_buttons(self, bool_value):
        self.btn_correspondence_add.setEnabled(bool_value)
        self.btn_correspondence_edit.setEnabled(bool_value)
        self.btn_correspondence_delete.setEnabled(bool_value)
        self.action_correspondence.setEnabled(bool_value)


