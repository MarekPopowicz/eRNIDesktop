# ComboBoxes
task_table_column_titles = ["Teczka", "Segment", "Nr SAP", "Priorytet", "Status", "Zadanie", "Inżynier", "Wpływ", "Kategoria",
                            "Sygnatura obca", "Termin do", "Aktywność", "Uwagi", "Link", ]
localization_table_column_titles = ["Numer KW", "AM", "Nr dz.", "Obręb", "Status", "Ulica", "Region", "Miejscowość", "Właściciel", "Link", ]
device_table_column_titles = ["Dł.", "Szer.", "Napięcie", "Urządzenie", "PSP", "Uwagi", ]
document_table_column_titles = ["Data", "Znak", "Nazwa dokumentu", "Wpływ", "Uwagi", "Plik"]
correspondence_table_column_titles = ['Kierunek', 'Wpływ', 'Nadawca/Adresat', 'Data', 'Znak', 'Dotyczy', 'Szablon', 'Typ']
activity_table_column_titles = ["Data", "Opis czynności", ]
invoice_table_column_titles = ["Data", "Numer", "Wystawca", "Tytuł", "Netto [zł.]", "Rejestracja", "SAP", "Uwagi", ]
regulation_table_column_titles = ["Wystawca", "Typ", "Data", "Numer", "Regulacja", "Koszt", "Oznaczenie dokumentu", "Uwagi", ]
property_document_table_column_titles = ["Typ", "Data", "Nr SAP", "Uwagi", ]

table_titles = {
    'task_table_column_titles': 'Zadania',
    'localization_table_column_titles': 'Lokalizacja',
    'device_table_column_titles': 'Urządzenia',
    'document_table_column_titles': 'Dokumentacja',
    'correspondence_table_column_titles': 'Korespondencja',
    'activity_table_column_titles': 'Czynności',
    'invoice_table_column_titles': 'Opłaty',
    'regulation_table_column_titles': 'Umowy',
    'property_document_table_column_titles': 'OT/PT', }

db_table_names = {
    'Zadania': 'tblProjects',
    'Lokalizacja': 'tblLocalizations',
    'Urządzenia': 'tblDevices',
    'Dokumentacja': 'tblKeyDocuments',
    'Korespondencja': 'tblProjectCorrespondence',
    'Czynności': 'tblActions',
    'Opłaty': 'tblInvoices',
    'Umowy': 'tblRegulations',
    'OT/PT': 'tblPropertyDocuments', }

tables_column_titles = {
    'task_table_column_titles': task_table_column_titles,
    'localization_table_column_titles': localization_table_column_titles,
    'device_table_column_titles': device_table_column_titles,
    'document_table_column_titles': document_table_column_titles,
    'correspondence_table_column_titles': correspondence_table_column_titles,
    'activity_table_column_titles': activity_table_column_titles,
    'invoice_table_column_titles': invoice_table_column_titles,
    'regulation_table_column_titles': regulation_table_column_titles,
    'property_document_table_column_titles': property_document_table_column_titles, }

# relation fields
relational_tables = {
    "statusName": ("statusId", "tblStatus"),
    "placeName": ("placeID", "tblPlaces"),
    "deviceCategoryName": ("deviceCategoryID", "tblDeviceCategories"),
    "keyDocumentName": ("KeyDocumentCategoryID", "tblKeyDocumentCategories"),
    "regulationCategoryName": ("regulationCategoryID", "tblRegulationCategories"),
    "projectCategoryName": ("projectCategoryID", "tblProjectCategories"),
    "regionName": ("regionId", "tblRegions"), }


def get_column_titles(table):
    for k, v in tables_column_titles.items():
        if k == table:
            return v


def get_table_db_name(table):
    for k, v in db_table_names.items():
        if k == table:
            return v


def get_table_titles(table):
    for k, v in table_titles.items():
        if v == table:
            return k