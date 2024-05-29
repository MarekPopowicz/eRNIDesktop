from PyQt5.QtCore import QModelIndex
from PyQt5.QtSql import QSqlRelationalDelegate, QSqlRelation
from PyQt5.QtWidgets import QDataWidgetMapper, QDesktopWidget

from db import Query
from utils import info_boxes


class Mapper:
    def __init__(self, manager, index, controls):
        self.manager = manager
        self.index = index
        self.current_row = 0
        self.model = manager.model
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setItemDelegate(QSqlRelationalDelegate())
        self.launch_controls = controls
        self.results = []

    def set_index(self, index):
        self.index = index
        if self.index is not None:  # edit
            self.select_item()
            self.current_row = self.index.row()
        else:  # add new
            self.current_row = self.add_new_row()
            self.model.setData(self.model.index(self.current_row, self.model.fieldIndex("projectID")),
                               self.manager.current_parent_row)  # set model data on current project id
        self.display_window_centered()

    def set_relation_field(self, tbl_rel_data, field_index, control, ctr_idx_pos=-1):
        self.model.setRelation(field_index, QSqlRelation(tbl_rel_data[0], tbl_rel_data[1], tbl_rel_data[2]))
        status_relModel = self.model.relationModel(field_index)
        control.setModel(status_relModel)
        control.setCurrentIndex(ctr_idx_pos)
        control.setModelColumn(status_relModel.fieldIndex(tbl_rel_data[2]))
        self.mapper.addMapping(control, field_index)

    def select_item(self):
        while self.model.canFetchMore():
            self.model.fetchMore()
        self.mapper.setCurrentModelIndex(self.index)

    def add_new_row(self):
        row = int(self.model.rowCount())  # finds which row is to add
        self.model.insertRow(row)  # creates new row
        index = QModelIndex(self.model.index(row, 0))
        self.mapper.setCurrentModelIndex(index)  # selects new row
        return row

    def set_header_info(self, lbl_projectId, lbl_task_name, project_id=None):
        if project_id is None:
            result = Query.get_project_data(self.manager.current_parent_row, self.manager.dbase)
        else:
            result = Query.get_project_data(project_id, self.manager.dbase)
        if not result:
            return
        lbl_projectId.setText(f'({result[0]}) {result[1]}')
        lbl_task_name.setText(result[2])

    @staticmethod
    def fill_combo(dbase, table, field, combo, command_type='select'):
        _list = Query.get_field_list(table, field, dbase, command_type)
        if not _list:
            pass
        else:
            _list.sort()
            combo.addItems(_list)
            combo.setCurrentIndex(-1)
        return combo

    def add_mapping(self, control, field_name):
        self.mapper.addMapping(control, self.model.fieldIndex(field_name))

    def closeEvent(self, event):
        self.manager.select_model()
        self.manager.table.setFocus()
        if self.manager.model.rowCount() > 0:
            self.manager.select_row()
        self.launch_controls.enable_buttons(True)

    def model_last_error_msg(self):

        # result = []
        # for col in range(self.mapper.model().columnCount()):
        #     val = self.mapper.model().data(self.mapper.model().index(0, col))
        #     result.append(val)

        msg = self.model.lastError().text()
        if len(msg) > 0:
            info_boxes.criticalBox("Błąd", msg)
        else:
            info_boxes.criticalBox("Błąd", "Coś poszło nie tak.")



    @staticmethod
    def validate_form(control_list):
        result = []
        for field in control_list:
            match field.__class__.__name__:
                case 'QComboBox':
                    if not field.currentText():
                        result.append(0)
                case 'QPlainTextEdit':
                    if not field.toPlainText():
                        result.append(0)
                case 'QDoubleSpinBox':
                    if field.value() == 0:
                        result.append(0)
                case 'QSpinBox':
                    if field.value() == 0:
                        result.append(0)
                case 'QLineEdit':
                    if not field.text():
                        result.append(0)
        if len(result) > 0:
            info_boxes.informationBox("Brak wymaganych informacji",
                                      "Nie wszystkie wymagane pola zostały prawidłowo wypełnione.")
            return False
        else:
            return True

    def display_window_centered(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def get_localization_data(self, row_count):
        _tuple = ()
        _list = list(_tuple)
        result = []

        for _row in range(row_count):
            for _col in range(2, 5):
                value = self.manager.parent.localization_manager.model.data(
                    self.manager.parent.localization_manager.model.index(_row, _col))
                _list.append(value)
            place = self.manager.parent.localization_manager.model.data(self.manager.parent.localization_manager.model.index(_row, 8))
            _list.append(place)
            _tuple = tuple(_list)
            result.append(_tuple)
            _list.clear()
        return result

    def set_localization_data(self, localization_data):
        if len(localization_data) > 0:
            result = [
                {localization_data[0][3]: [(localization_data[0][2], localization_data[0][0], [localization_data[0][1]])]}]

            for item in localization_data:
                for k in result:
                    if item[3] not in k.keys():
                        result.append({item[3]: [(item[2], item[0], [item[1]])]})
                    else:
                        for i in result:
                            for _key, _val in i.items():
                                for j in range(len(_val)):
                                    obr = _val[j][0]
                                    am = _val[j][1]
                                    dz = _val[j][2]
                                    if _key == item[3]:
                                        if not self.if_element_exist(_val, item[2]):
                                            _val.append((item[2], item[0], [item[1]]))
                                        elif not self.if_element_exist(_val, item[0]) and self.if_element_exist(_val,
                                                                                                                item[2]):
                                            _val.append((item[2], item[0], [item[1]]))
                                        elif obr == item[2] and am == item[0] and (item[1] not in dz):
                                            dz.append(item[1])
                                    else:
                                        continue
            localization = ''
            for r in result:
                for k, v in r.items():
                    for q in v:
                        localization = localization + f'dz. {", ".join(str(x) for x in q[2])} AM-{int(q[1])} obr. {q[0]}; '
                    localization = localization + k + '; '
            return localization
        else:
            return False

    @staticmethod
    def if_element_exist(_list, _element):
        result = False
        for el in range(len(_list)):
            if _element in _list[el]:
                result = True
        return result