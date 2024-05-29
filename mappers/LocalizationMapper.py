from PyQt5.QtCore import Qt, QEvent, QDate
from PyQt5.QtWidgets import QDialog
from inspectors import OwnerInspector
from managers import AddressBookManager
from mappers import DeviceMapper, Mapper
from ui.localization_mapper import Ui_Form

class LocalizationMapper(QDialog, Ui_Form, Mapper.Mapper):
    def __init__(self, manager, controls, localization_idx=None):
        QDialog.__init__(self)
        Ui_Form.__init__(self)

        if controls.__class__.__name__=='LocalizationControl':
            Mapper.Mapper.__init__(self, manager, localization_idx, controls)
            self.device_mapper = DeviceMapper.DeviceMapper(self.manager.device_manager, controls.device_controls)
        else:
            Mapper.Mapper.__init__(self, manager, localization_idx, controls[0])
            self.device_mapper = DeviceMapper.DeviceMapper(self.manager.device_manager, controls[1])
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # destroy window object on close
        self.owner_inspector = None
        self.addressbook = None
        self.agent = manager.restorationAgent
        if len(self.agent.data)>0:
            self.btn_restore.setEnabled(True)
        self.txt_register.installEventFilter(self)

        # set mapped fields and controls
        self.set_relation_field(["tblStatus", "StatusId", "statusName"], self.model.fieldIndex("statusName"), self.cbo_status, 5)
        self.add_mapping(self.txt_register, "localizationLandRegister")
        self.add_mapping(self.txt_parcel, "localizationPlotNo")
        self.add_mapping(self.spb_map, "localizationMapNo")
        self.fill_combo(self.manager.dbase, 'tblPrecincts', 'localizationPrecinct', self.cbo_area)
        self.add_mapping(self.cbo_area, "localizationPrecinct")
        self.add_mapping(self.txt_street, "localizationStreets")
        self.set_relation_field(["tblPlaces", "placeID", "placeName"], self.model.fieldIndex("placeName"), self.cbo_place)
        self.cbo_place.model().sort(1, Qt.AscendingOrder)
        self.set_relation_field(["tblRegions", "regionId", "regionName"], self.model.fieldIndex("regionName"), self.cbo_region)
        self.add_mapping(self.txt_link, "localizationLink")
        self.add_mapping(self.txt_name, "ownerName")
        self.add_mapping(self.txt_additional_info, "localizationAdditionalInfo")

        # set slots and signals
        self.btn_addressbook.clicked.connect(self.addressbook_open)
        self.btn_owner_inspector.clicked.connect(self.owner_inspector_open)
        self.btn_ok.clicked.connect(self.on_submit)
        self.btn_restore.clicked.connect(self.on_restore)


    def clear_controls(self):
        self.txt_register.clear()
        self.cbo_status.setCurrentIndex(-1)
        self.spb_map.setValue(0)
        self.cbo_region.setCurrentIndex(-1)
        self.txt_register.setText('WR1K/')
        self.cbo_status.setFocus()

    def owner_inspector_open(self):
        if self.owner_inspector is None:
            self.owner_inspector = OwnerInspector.OwnerInspector(self.manager.dbase, parent=self)
        self.owner_inspector.set_position()
        self.owner_inspector.load_data()
        self.owner_inspector.show()

    def addressbook_open(self):
        if self.addressbook is None:
            self.addressbook = AddressBookManager.AddresseeManager(self.manager.dbase, None)
        self.addressbook.show_addressbook('external')

    def on_submit(self):
        if self.validate_form(
                [self.spb_map, self.cbo_status, self.cbo_region, self.cbo_area, self.cbo_place, self.txt_register, self.txt_parcel,
                 self.txt_name]):
            if self.mapper.submit():
                self.agent.clearValues()
                self.btn_restore.setEnabled(False)
                if not self.manager.parent.tabs_case_segments.isTabEnabled(0):
                    self.manager.parent.tabs_case_segments.setTabEnabled(0, True)
                    self.manager.parent.tabs_case_segments.setCurrentIndex(0)
                self.close()
                if self.manager.table.model().rowCount() > 0 and self.index is None:
                    self.manager.select_row(self.manager.model.rowCount() - 1)  # point on new inserted row
                    self.device_mapper.set_index(None)  # add new device
                    self.device_mapper.show()
            else:
                self.model_last_error_msg()
                self.catch_data()
                self.close()

    def catch_data(self):
        self.agent.clearValues()
        self.agent.pushValue(self.cbo_status.currentText())
        self.agent.pushValue(self.txt_register.text())
        self.agent.pushValue(self.txt_parcel.text())
        self.agent.pushValue(self.spb_map.value())
        self.agent.pushValue(self.txt_street.text())
        self.agent.pushValue(self.cbo_place.currentIndex())
        self.agent.pushValue(self.cbo_area.currentText())
        self.agent.pushValue(self.cbo_region.currentText())
        self.agent.pushValue(self.txt_link.text())
        self.agent.pushValue(self.txt_name.toPlainText())
        self.agent.pushValue(self.txt_additional_info.toPlainText())


    def on_restore(self):
        values = self.agent.getValues()
        self.cbo_status.setCurrentText(values[0])
        self.txt_register.setText(values[1])
        self.txt_parcel.setText(values[2])
        self.spb_map.setValue(values[3])
        self.txt_street.setText(values[4])
        self.cbo_place.setCurrentIndex(values[5])
        self.cbo_area.setCurrentText(values[6])
        self.cbo_region.setCurrentText(values[7])
        self.txt_link.setText(values[8])
        self.txt_name.setPlainText(values[9])
        self.txt_additional_info.setPlainText(values[10])


    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if source is self.txt_register and (event.key() == Qt.Key.Key_Escape):
                self.txt_register.setText('Brak danych')
        return super(LocalizationMapper, self).eventFilter(source, event)