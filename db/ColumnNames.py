# sql_query
task_db_fields = 'tblProjects.projectID, ' \
                 'projectSegment, ' \
                 'projectSapNo, ' \
                 'projectPriority, ' \
                 'tblProjects.statusName, ' \
                 'projectTask, ' \
                 'projectManager, ' \
                 'projectInflow, ' \
                 'projectCategoryName, ' \
                 'projectForeignSignature, ' \
                 'projectDeadLine, ' \
                 'projectLastActivity, ' \
                 'projectAdditionalInfo, ' \
                 'projectLink '

# table headers translation
task_table_column_titles = {
    "projectID": "Teczka",
    "projectSegment": "Segment",
    "projectSapNo": "Nr SAP",
    "projectPriority": "Priorytet",
    "statusName": "Status",
    "projectTask": "Zadanie",
    "projectManager": "Inżynier",
    "projectInflow": "Wpływ",
    "projectCategoryName": "Kategoria",
    "projectForeignSignature": "Sygnatura obca",
    "projectDeadLine": "Termin do",
    "projectLastActivity": "Aktywność",
    "projectAdditionalInfo": "Uwagi",
    "projectLink": "Link",
}

localization_table_column_titles = {
    "localizationID": "Id",
    "localizationLandRegister": "Numer KW",
    "localizationMapNo": "AM",
    "localizationPlotNo": "Nr dz.",
    "localizationPrecinct": "Obręb",
    "statusName": "Status",
    "localizationStreets": "Ulica",
    "regionName": "Region",
    "placeName": "Miejscowość",
    "projectID": "Teczka",
    "localizationLink": "Link",
    "localizationAdditionalInfo": "Uwagi",
    "ownerName": "Właściciel",
}

device_table_column_titles = {
    "deviceID": "Id",
    "deviceLenght": "Dł.",
    "deviceWidth": "Szer.",
    "deviceVoltage": "Napięcie",
    "deviceCategoryName": "Urządzenie",
    "localizationID": "Lokalizacja",
    "deviceAdditionalInfo": "Uwagi",
    "devicePSPelement": "PSP",
    "projectID": "Teczka",
}

document_table_column_titles = {
    "keyDocumentID": "Id",
    "keyDocumentDate": "Data",
    "keyDocumentSign": "Znak",
    "keyDocumentName": "Nazwa dokumentu",
    "keyDocumentObtainment": "Wpływ",
    "projectID": "Teczka",
    "keyDocumentAdditionalInfo": "Uwagi",
    "keyDocumentFile": "Plik"
}

correspondence_table_column_titles = {
    'projectCorrespondenceID': 'Id',
    'projectCorrespondenceDirection': 'Kierunek',
    'projectCorrespondenceSender': 'Nadawca/Adresat',
    'projectCorrespondenceTemplate': 'Szablon',
    'projectCorrespondenceDate': 'Data',
    'projectCorrespondenceSign': 'Znak',
    'projectCorrespondenceSubject': 'Dotyczy',
    'projectCorrespondenceObtainment': 'Wpływ',
    'projectID': 'Teczka',
    'documentSign': 'Dokument szablonu',
    'projectCorrespondenceType': 'Typ',
    'projectCorrespondenceInfo': 'Informacja'
}

activity_table_column_titles = {
    "actionID": "Id",
    "actionDate": "Data",
    "actionDescription": "Opis czynności",
    "projectID": "Teczka",
    "actionKeepAttention": "Obserwuj"
}

invoice_table_column_titles = {
    "invoiceID": "Id",
    "invoiceAdditionalInfo": "Uwagi",
    "invoiceIssueDate": "Data",
    "invoiceNettoValue": "Netto [zł.]",
    "invoiceTax": "VAT [%]",
    "invoiceNo": "Numer",
    "invoiceSapRegisterNo": "SAP",
    "invoiceSapRegistrationDate": "Rejestracja",
    "invoiceSellerName": "Wystawca",
    "invoiceTitle": "Tytuł",
    "projectID": "Teczka",

}

regulation_table_column_titles = {
    "regulationDocumentID": "Id",
    "projectID": "Teczka",
    "regulationSapElement": "Element",
    "regulationDocumentDate": "Data",
    "regulationDocumentSignature": "Numer",
    "regulationDocumentSource": "Wystawca",
    "regulationDocumentType": "Typ",
    "regulationCategoryName": "Regulacja",
    "regulationCost": "Koszt",
    "regulationDocumentLink": "Oznaczenie dokumentu",
    "additionalInformation": "Uwagi",
}

property_document_table_column_titles = {
    "propertyDocumentID": "Id",
    "propertyDocumentAdditionalInfo": "Uwagi",
    "propertyDocumentSapRegisterNo": "Nr SAP",
    "propertyDocumentSapRegistrationDate": "Data",
    "propertyDocumentType": "Typ",
    "projectID": "Teczka",
}

todo_table_column_titles = {
    "todoId": "Id",
    "todoTaskCase": "Teczka",
    "todoRegistrationDate": "Data Wpisu",
    "todoItem": "Do zrobienia",
    "todoDeadLine": "Termin",
}

db_tables_column_titles = {
    'task_table_column_titles': task_table_column_titles,
    'localization_table_column_titles': localization_table_column_titles,
    'device_table_column_titles': device_table_column_titles,
    'document_table_column_titles': document_table_column_titles,
    'correspondence_table_column_titles': correspondence_table_column_titles,
    'activity_table_column_titles': activity_table_column_titles,
    'invoice_table_column_titles': invoice_table_column_titles,
    'regulation_table_column_titles': regulation_table_column_titles,
    'property_document_table_column_titles': property_document_table_column_titles,
}

reports_table_column_titles = {
    "reportID": "Nr",
    "reportName": "Nazwa",
    "reportDefinition": "Definicja",
    "reportDescription": "Opis",
    "reportOutput": "Format",
}


def get_db_column_titles(table):
    for k, v in db_tables_column_titles.items():
        if k == table:
            return v


def get_db_column_name(var, col):
    for k, v in var.items():
        if v == col:
            return k