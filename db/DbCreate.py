import os
from db import DbDefinition
from utils import file_io, info_boxes


def create_database(connection):
    connection.exec(DbDefinition.create_tblInternalAddressee)
    connection.exec(DbDefinition.create_tblExternalsAddressee)
    connection.exec(DbDefinition.create_tblCollaborativeAddressee)

    connection.exec(DbDefinition.create_tblRegulationCategories)
    connection.exec(DbDefinition.create_tblProjectTaskCategories)
    connection.exec(DbDefinition.create_tblKeyDocumentCategories)
    connection.exec(DbDefinition.create_tblInvoiceCategories)
    connection.exec(DbDefinition.create_tblDeviceCategories)
    connection.exec(DbDefinition.create_tblActivityCategories)
    connection.exec(DbDefinition.create_tblProjectCategories)
    connection.exec(DbDefinition.create_tblStatus)

    connection.exec(DbDefinition.create_tblProjects)
    connection.exec(DbDefinition.create_tblLocalizations)
    connection.exec(DbDefinition.create_tblDevices)
    connection.exec(DbDefinition.create_tblKeyDocuments)
    connection.exec(DbDefinition.create_tblProjectCorrespondence)
    connection.exec(DbDefinition.create_tblActions)
    connection.exec(DbDefinition.create_tblInvoices)
    connection.exec(DbDefinition.create_tblRegulations)
    connection.exec(DbDefinition.create_tblPropertyDocuments)

    connection.exec(DbDefinition.create_tblStreets)
    connection.exec(DbDefinition.create_tblRegions)
    connection.exec(DbDefinition.create_tblPrecincts)
    connection.exec(DbDefinition.create_tblPlaces)
    connection.exec(DbDefinition.create_tblProjectManagers)
    connection.exec(DbDefinition.create_tblPSPelement)
    connection.exec(DbDefinition.create_tblEmailTemplates)
    connection.exec(DbDefinition.create_tblDocumentsTemplates)
    connection.exec(DbDefinition.create_tblReports)
    connection.exec(DbDefinition.create_view_main_report)
    connection.exec(DbDefinition.create_tblToDo)

    return True


def create_folders():
    home = os.path.expanduser("~")
    basedir = os.path.dirname(__file__)
    try:
        file_io.create_folder(home + '\\eRNI\\Repos')  # Repository folder
        file_io.create_folder(home + '\\eRNI\\MailTempl')  # Mail templates
        file_io.create_folder(home + '\\eRNI\\DocsTempl')  # Document templates
        file_io.create_folder(home + '\\eRNI\\DocsTempl\\Images')  # Images folder
        source_file = os.path.dirname(basedir) + '\\res\\icon\\td_logo.png'
        destination = home + '\\eRNI\\DocsTempl\\Images'
        file_io.copy_file(source_file, destination)  # copy logo image
        file_io.create_folder(home + '\\eRNI\\Reports')  # Reports folder

        return True
    except:
        info_boxes.criticalBox("Błąd operacji.", f"Nieudana próba utworzenia kalalogów roboczych w folderze użytkownika: {home}")
        return False