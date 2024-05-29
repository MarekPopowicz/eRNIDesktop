import webbrowser
from PyQt5 import QtCore
from controls import Controls
from db import Query, DbData
from generators import DocumentTagGenerator
from mappers import DocumentMapper
from utils import info_boxes, file_io


class DocumentControl(Controls.Controls):
    def __init__(self, controls, table_manager):
        super().__init__(table_manager)
        self.btn_document_add = controls[0]
        self.btn_document_edit = controls[1]
        self.btn_document_delete = controls[2]
        self.btn_documents_print = controls[3]
        self.btn_documentation_label = controls[4]
        self.actionDokumentacja = controls[5]
        self.action_document_file_tag = controls[6]

        self.mapper = DocumentMapper.DocumentMapper(self.manager, self)
        self.file_tag_generator = None

        self.btn_document_add.clicked.connect(self.add_document_mapper)
        self.btn_document_edit.clicked.connect(self.edit_document_mapper)
        self.btn_document_delete.clicked.connect(self.remove_document)
        self.btn_documents_print.clicked.connect(self.print_documents)
        self.btn_documentation_label.clicked.connect(self.print_docs_label)
        self.actionDokumentacja.triggered.connect(self.add_document_mapper)
        self.action_document_file_tag.triggered.connect(self.tag_generator)

    def remove_document(self):
        result = self.remove_row()

        if result is None or result == -1 or result == True:
            return

        else:  # no more rows - disable controls
            self.manager.parent.tabs_case_segments.setTabEnabled(1, False)
    def edit_document_mapper(self):
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(self.manager.table.currentIndex())  # set current table index to edit data
        self.mapper.show()
        self.enable_buttons(False)

    def add_document_mapper(self):
        if self.manager.parent.model.rowCount() == 0:
            return
        self.mapper.set_header_info(self.mapper.lbl_projectId, self.mapper.lbl_task_name)
        self.mapper.set_index(None)
        self.mapper.set_controls()
        self.mapper.show()
        self.enable_buttons(False)


    def tag_generator(self):
        doc_id = self.get_document_id()
        if not doc_id:
            info_boxes.criticalBox('Brak dokumentu',
                                   "Brak dokumentu uniemożliwia wykonanie operacji.")
            return

        if self.file_tag_generator is None:
            self.file_tag_generator = DocumentTagGenerator.DocumentTagGenerator(self)
        else:
            self.file_tag_generator.db = self.manager.dbase
            self.file_tag_generator.doc_data = self.generate_file_tag()
            if self.file_tag_generator.doc_data is None:
                return
            self.file_tag_generator.doc_id = self.get_document_id()
            self.file_tag_generator.set_document_data()
        self.file_tag_generator.show()


    def get_document_id(self):
        if not self.manager.current_row() is None:
            idx = self.manager.model.index(self.manager.current_row(), 0)
            value = self.manager.model.data(idx)
            return value
        else:
            return False


    def generate_file_tag(self):
        doc_data = []
        sap_no = self.manager.parent.model.data(self.manager.parent.model.index(self.manager.parent.current_row(),
                                                                                    self.manager.parent.model.fieldIndex(
                                                                                        "projectSapNo")))
        _id = self.manager.parent.model.data(self.manager.parent.model.index(self.manager.parent.current_row(),
                                                                                self.manager.parent.model.fieldIndex(
                                                                                    "projectID")))
        if self.manager.model.rowCount() > 0:
            doc_data.append(_id)
            doc_data.append(sap_no)  # 0

            for item in range(self.manager.model.columnCount()):
                idx = self.manager.model.index(self.manager.current_row(), item)
                if item in (self.manager.model.fieldIndex("keyDocumentSign"),
                            self.manager.model.fieldIndex("keyDocumentDate"),
                            self.manager.model.fieldIndex("keyDocumentName")
                            ):
                    value = self.manager.model.data(idx)
                    doc_data.append(value)

            return doc_data

    def print_docs_label(self):
        path_repository = self.manager.parent.settings[2] + '\\' + str(self.manager.current_parent_row)
        document = DbData.label

        leader = self.manager.parent.settings[4]
        if leader == '':
            info_boxes.criticalBox('Wydruk etykiety',
                                   'Brak informacji o prowadzącym sprawę.\n'
                                   'Należy uzupełnić dane o użytkowniku w ustawieniach aplikacji.')
            return

        document = document.replace('[leader]', leader)
        localization = self.mapper.get_localization_data(self.manager.parent.localization_manager.row_count())
        if len(localization)==0:
            info_boxes.criticalBox('Wydruk etykiety',
                                   'Brak informacji o lokalizacji urządzeń.\n'
                                   'Należy uzupełnić dane.')
            return
        document = document.replace('[localization]', self.get_localization_data(localization))

        owner = self.get_owner()
        if owner == '':
            info_boxes.criticalBox('Wydruk etykiety',
                                   'Brakuje informacji  o właścicielu nieruchomości.\n'
                                   'Należy najpierw uzupełnić dane.')
            return

        contacts = self.get_owner_contacts(owner)

        if not contacts:
            owner = owner.replace('\n','<br>')
            owner = owner.replace(owner, f'<div style = "margin-left: 5%; margin-top: 10px; color: darkblue; text-shadow: 2px 2px 5px rgb(94, 92, 92);">{owner}</div>')
            string = '''
                        <div><span class="symbol">&#129333;</span><span id="name">[owner]</span></div>
                        <div><span class="symbol">&#9993;</span><span id="mail">[mail]</span>
                            <span class="symbol">&#9742;</span> <span id="phone">[phone]</span>     
                            <span class="symbol">&#9990;</span> <span id="phone">[mobile]</span>'''
            document = document.replace(string, owner)
        else:
            document = document.replace('[owner]', owner)
            if contacts[0] == '':
                document = document.replace('[phone]', 'Brak informacji')
            else:
                document = document.replace('[phone]', contacts[0])

            if contacts[1] == '':
                document = document.replace('[mobile]', 'Brak informacji')
            else:
                document = document.replace('[mobile]', contacts[1])

            if contacts[2] == '':
                document = document.replace('[mail]', 'Brak informacji')
            else:
                document = document.replace('[mail]', contacts[2])

        project_information = self.get_project_info()
        document = document.replace('[task]', project_information[0])
        document = document.replace('[case]', '(' + str(project_information[1]) + ')')
        document = document.replace('[segment]', project_information[2])
        document = document.replace('[priority]', project_information[3])
        if project_information[3] == 'Tak':
            document = document.replace('flag_No', 'flag_Yes')

        document = document.replace('[label]', project_information[4])
        document = document.replace('[sap]', project_information[4])
        document = document.replace('[manager]', project_information[5])

        document = document.replace('[data]', self.manager.current_date.toString(QtCore.Qt.ISODate))
        label = f'({str(project_information[1])}) {project_information[4]} Etykieta projektu.htm'
        if not file_io.write_file(path_repository + '\\' + label, document):
            file_io.create_folder(path_repository)
            file_io.write_file(path_repository + '\\' + label, document)
        webbrowser.open(path_repository + '\\' + label)

    def get_owner(self):
        name = self.manager.parent.localization_manager.model.fieldIndex('ownerName')
        idx = self.manager.parent.localization_manager.model.index(0, name)
        owner = self.manager.parent.localization_manager.model.data(idx)
        return owner

    def get_owner_contacts(self, owner):
        qry = f"SELECT * FROM tblExternalsAddressee WHERE addresseeName = '{owner}'"
        data = Query.get_data(self.manager.dbase, qry, 11)
        if not data:
            return False
        else:
            contacts = (data[0][4], data[0][5], data[0][8])
            return contacts

    def get_project_info(self):
        task = self.get_project_data('projectTask')
        sap = self.get_project_data('projectSapNo')
        case = self.get_project_data('projectID')
        segment = self.get_project_data('projectSegment')
        priority = self.get_project_data('projectPriority')
        manager = self.get_project_data('projectManager')
        return task, case, segment, priority, sap, manager

    def print_documents(self):
        caption_text = f'<span style = "color: #c71b38;">({self.get_project_data("projectID")})</span> <span>{self.get_project_data("projectSapNo")}</span><span style = "padding: 10px 10px"> Dokumenty</span>'
        self.print('documents_report', caption_text, self.get_project_data("projectID"))

    @staticmethod
    def get_localization_data(localization_data):
        localization = ''
        for item in localization_data:
            localization = localization + f'<li> <strong>dz.</strong> {item[1]}, <strong>AM</strong> {int(item[0])}, <strong>obr. </strong>{item[2]}; {item[3]}</li>'
        return localization


    @staticmethod
    def if_element_exist(_list, _element):
        result = False
        for el in range(len(_list)):
            if _element in _list[el]:
                result = True
        return result

    def enable_buttons(self, bool_value):
        self.btn_document_add.setEnabled(bool_value)
        self.btn_document_edit.setEnabled(bool_value)
        self.btn_document_delete.setEnabled(bool_value)
        self.actionDokumentacja.setEnabled(bool_value)