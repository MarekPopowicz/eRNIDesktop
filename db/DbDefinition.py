# SQL Table definitions
# 1
create_tblInternalAddressee = 'CREATE TABLE IF NOT EXISTS "tblInternalAddressee" (' \
                              '"addresseeID"	INTEGER,' \
                              '"addresseeName"	TEXT NOT NULL UNIQUE,' \
                              '"addresseeHouseNo"	TEXT NOT NULL,' \
                              '"addresseeAptNo"	TEXT,' \
                              '"addresseePhone"	TEXT,' \
                              '"addresseeCellPhone"	TEXT,' \
                              '"addresseePostOffice"	TEXT NOT NULL,' \
                              '"addresseeZipCode"	TEXT NOT NULL,' \
                              '"addresseeEmail"	TEXT,' \
                              '"addresseeCity"	TEXT NOT NULL,' \
                              '"addresseeStreet"	TEXT,' \
                              'PRIMARY KEY("addresseeID" AUTOINCREMENT)' \
                              ')'
# 2
create_tblExternalsAddressee = 'CREATE TABLE IF NOT EXISTS "tblExternalsAddressee" (' \
                               '"addresseeID"	INTEGER,' \
                               '"addresseeName"	TEXT NOT NULL UNIQUE,' \
                               '"addresseeHouseNo"	TEXT NOT NULL,' \
                               '"addresseeAptNo"	TEXT,' \
                               '"addresseePhone"	TEXT,' \
                               '"addresseeCellPhone"	TEXT,' \
                               '"addresseePostOffice"	TEXT NOT NULL,' \
                               '"addresseeZipCode"	TEXT NOT NULL,' \
                               '"addresseeEmail"	TEXT,' \
                               '"addresseeCity"	TEXT NOT NULL,' \
                               '"addresseeStreet"	TEXT,' \
                               'PRIMARY KEY("addresseeID" AUTOINCREMENT)' \
                               ')'
# 3
create_tblCollaborativeAddressee = 'CREATE TABLE IF NOT EXISTS "tblCollaborativeAddressee" (' \
                                   '"addresseeID"	INTEGER,' \
                                   '"addresseeName"	TEXT NOT NULL UNIQUE,' \
                                   '"addresseeHouseNo"	TEXT NOT NULL,' \
                                   '"addresseeAptNo"	TEXT,' \
                                   '"addresseePhone"	TEXT,' \
                                   '"addresseeCellPhone"	TEXT,' \
                                   '"addresseePostOffice"	TEXT NOT NULL,' \
                                   '"addresseeZipCode"	TEXT NOT NULL,' \
                                   '"addresseeEmail"	TEXT,' \
                                   '"addresseeCity"	TEXT NOT NULL,' \
                                   '"addresseeStreet"	TEXT,' \
                                   'PRIMARY KEY("addresseeID" AUTOINCREMENT)' \
                                   ')'
# 4
create_tblRegulationCategories = 'CREATE TABLE IF NOT EXISTS "tblRegulationCategories" (' \
                                 '"regulationCategoryID"	INTEGER,' \
                                 '"regulationCategoryName"	TEXT NOT NULL,' \
                                 'PRIMARY KEY("regulationCategoryID" AUTOINCREMENT)' \
                                 ')'
# 5
create_tblProjectTaskCategories = 'CREATE TABLE IF NOT EXISTS "tblProjectTaskCategories" (' \
                                  '"projectTaskCategoryId"	INTEGER,' \
                                  '"projectTaskName"	TEXT NOT NULL,' \
                                  'PRIMARY KEY("projectTaskCategoryId")' \
                                  ')'
# 6
create_tblKeyDocumentCategories = 'CREATE TABLE IF NOT EXISTS "tblKeyDocumentCategories" (' \
                                  '"KeyDocumentCategoryID"	INTEGER,' \
                                  '"keyDocumentName"	TEXT NOT NULL,' \
                                  'PRIMARY KEY("KeyDocumentCategoryID" AUTOINCREMENT)' \
                                  ')'
# 7
create_tblInvoiceCategories = 'CREATE TABLE IF NOT EXISTS "tblInvoiceCategories" (' \
                              '"invoiceCategoryId"	INTEGER,' \
                              '"invoiceTitle"	TEXT NOT NULL,' \
                              'PRIMARY KEY("invoiceCategoryId" AUTOINCREMENT)' \
                              ')'
# 8
create_tblDeviceCategories = 'CREATE TABLE IF NOT EXISTS "tblDeviceCategories" (' \
                             '"deviceCategoryID"	INTEGER,' \
                             '"deviceCategoryName"	TEXT NOT NULL,' \
                             'PRIMARY KEY("deviceCategoryID" AUTOINCREMENT)' \
                             ')'
# 9
create_tblActivityCategories = 'CREATE TABLE IF NOT EXISTS "tblActivityCategories" (' \
                               '"ActivityCategoryID"	INTEGER,' \
                               '"ActivityName"	TEXT NOT NULL,' \
                               'PRIMARY KEY("ActivityCategoryID" AUTOINCREMENT)' \
                               ')'
# 10
create_tblProjectCategories = 'CREATE TABLE IF NOT EXISTS "tblProjectCategories" (' \
                              '"projectCategoryID"	INTEGER,' \
                              '"projectCategoryName"	TEXT NOT NULL,' \
                              'PRIMARY KEY("projectCategoryID" AUTOINCREMENT)' \
                              ')'
# 11
create_tblStatus = 'CREATE TABLE IF NOT EXISTS "tblStatus" (' \
                   '"statusID"	INTEGER,' \
                   '"statusName"	TEXT NOT NULL UNIQUE,' \
                   'PRIMARY KEY("statusID" AUTOINCREMENT)' \
                   ')'
# 12
create_tblProjects = 'CREATE TABLE IF NOT EXISTS "tblProjects" (' \
                     '"projectID"	INTEGER NOT NULL UNIQUE,' \
                     '"projectSegment"	TEXT NOT NULL,' \
                     '"projectSapNo"	TEXT NOT NULL,' \
                     '"projectPriority"	INTEGER NOT NULL,' \
                     '"statusName"	INTEGER NOT NULL,' \
                     '"projectTask"	TEXT NOT NULL,' \
                     '"projectManager"	TEXT NOT NULL,' \
                     '"projectInflow"	TEXT NOT NULL,' \
                     '"projectCategoryName"	INTEGER NOT NULL,' \
                     '"projectForeignSignature"	TEXT,' \
                     '"projectDeadLine"	TEXT,' \
                     '"projectLastActivity"	TEXT,' \
                     '"projectAdditionalInfo"	TEXT,' \
                     '"projectLink"	TEXT,' \
                     'PRIMARY KEY("projectID"),' \
                     'FOREIGN KEY("statusName") REFERENCES "tblStatus"("statusID"),' \
                     'FOREIGN KEY("projectCategoryName") REFERENCES "tblProjectCategories"("projectCategoryID")' \
                     ')'
# 13
create_tblLocalizations = 'CREATE TABLE IF NOT EXISTS "tblLocalizations" (' \
                          '"localizationID"	INTEGER,' \
                          '"localizationLandRegister"	REAL NOT NULL,' \
                          '"localizationMapNo"	INTEGER NOT NULL,' \
                          '"localizationPlotNo"	TEXT NOT NULL,' \
                          '"localizationPrecinct"	TEXT NOT NULL,' \
                          '"statusName"	INTEGER NOT NULL,' \
                          '"localizationStreets"	TEXT,' \
                          '"localizationRegion"	TEXT NOT NULL,' \
                          '"placeName"	INTEGER NOT NULL,' \
                          '"projectID"	INTEGER NOT NULL,' \
                          '"localizationLink"	TEXT,' \
                          '"localizationAdditionalInfo"	TEXT,' \
                          '"ownerName"	TEXT,' \
                          'FOREIGN KEY("projectID") REFERENCES "tblProjects",' \
                          'PRIMARY KEY("localizationID" AUTOINCREMENT)' \
                          ')'
# 14
create_tblDevices = 'CREATE TABLE IF NOT EXISTS "tblDevices" (' \
                    '"deviceID"	INTEGER,' \
                    '"deviceLenght"	REAL NOT NULL,' \
                    '"deviceWidth"	REAL NOT NULL,' \
                    '"deviceVoltage"	INTEGER NOT NULL,' \
                    '"deviceCategoryName"	INTEGER NOT NULL,' \
                    '"localizationID"	INTEGER NOT NULL,' \
                    '"deviceAdditionalInfo"	TEXT,' \
                    '"devicePSPelement"	TEXT,' \
                    '"projectID"	INTEGER NOT NULL,' \
                    'PRIMARY KEY("deviceID"),' \
                    'FOREIGN KEY("localizationID") REFERENCES "tblLocalizations"("localizationID") ON UPDATE CASCADE ON DELETE CASCADE' \
                    ')'
# 15
create_tblKeyDocuments = 'CREATE TABLE IF NOT EXISTS "tblKeyDocuments" (' \
                         '"keyDocumentID"	INTEGER,' \
                         '"keyDocumentDate"	TEXT NOT NULL,' \
                         '"keyDocumentSign"	TEXT NOT NULL,' \
                         '"keyDocumentName"	INTEGER NOT NULL,' \
                         '"keyDocumentObtainment"	TEXT NOT NULL,' \
                         '"projectID"	INTEGER NOT NULL,' \
                         '"keyDocumentAdditionalInfo"	TEXT,' \
                         '"keyDocumentFile"	TEXT,' \
                         'FOREIGN KEY("keyDocumentName") REFERENCES "tblKeyDocumentCategories"("KeyDocumentCategoryID"),' \
                         'PRIMARY KEY("keyDocumentID")' \
                         ')'
# 16
create_tblProjectCorrespondence = 'CREATE TABLE IF NOT EXISTS "tblProjectCorrespondence" (' \
                                  '"projectCorrespondenceID"	INTEGER,' \
                                  '"projectCorrespondenceDirection"	TEXT NOT NULL,' \
                                  '"projectCorrespondenceSender"	TEXT NOT NULL,' \
                                  '"projectCorrespondenceTemplate"	TEXT,' \
                                  '"projectCorrespondenceDate"	TEXT NOT NULL,' \
                                  '"projectCorrespondenceSign"	TEXT NOT NULL,' \
                                  '"projectCorrespondenceSubject"	TEXT NOT NULL,' \
                                  '"projectCorrespondenceObtainment"	TEXT NOT NULL,' \
                                  '"projectID"	INTEGER NOT NULL,' \
                                  '"documentSign"	TEXT,' \
                                  '"projectCorrespondenceType"	TEXT,' \
                                  '"projectCorrespondenceInfo"	TEXT,' \
                                  'PRIMARY KEY("projectCorrespondenceID")' \
                                  ')'
# 17
create_tblActions = 'CREATE TABLE "tblActions" (' \
                    '"actionID"	INTEGER,' \
                    '"actionDate"	TEXT NOT NULL,' \
                    '"actionDescription"	TEXT NOT NULL,' \
                    '"projectID"	INTEGER NOT NULL,' \
                    '"actionKeepAttention"	INTEGER NOT NULL DEFAULT 0,' \
                    'PRIMARY KEY("actionID")' \
                    ')'
# 18
create_tblInvoices = 'CREATE TABLE IF NOT EXISTS "tblInvoices" (' \
                     '"invoiceID"	INTEGER,' \
                     '"invoiceAdditionalInfo"	TEXT,' \
                     '"invoiceIssueDate"	TEXT NOT NULL,' \
                     '"invoiceNettoValue"	REAL NOT NULL,' \
                     '"invoiceTax"	REAL NOT NULL,' \
                     '"invoiceNo"	TEXT NOT NULL,' \
                     '"invoiceSapRegisterNo"	TEXT NOT NULL,' \
                     '"invoiceSapRegistrationDate"	TEXT NOT NULL,' \
                     '"invoiceSellerName"	TEXT NOT NULL,' \
                     '"invoiceTitle"	TEXT NOT NULL,' \
                     '"projectID"	INTEGER NOT NULL,' \
                     'FOREIGN KEY("projectID") REFERENCES "tblProjects"("projectID"),' \
                     'PRIMARY KEY("invoiceID" AUTOINCREMENT)' \
                     ')'
# 19
create_tblRegulations = 'CREATE TABLE IF NOT EXISTS "tblRegulations" (' \
                        '"regulationDocumentID"	INTEGER,' \
                        '"projectID"	INTEGER NOT NULL,' \
                        '"regulationSapElement"	TEXT NOT NULL,' \
                        '"regulationDocumentDate"	TEXT NOT NULL,' \
                        '"regulationDocumentSignature"	TEXT NOT NULL,' \
                        '"regulationDocumentSource"	TEXT NOT NULL,' \
                        '"regulationDocumentType"	TEXT NOT NULL,' \
                        '"regulationCategoryName"	INTEGER NOT NULL,' \
                        '"regulationCost"	REAL NOT NULL,' \
                        '"regulationDocumentLink"	TEXT,' \
                        '"additionalInformation"	TEXT,' \
                        'PRIMARY KEY("regulationDocumentID" AUTOINCREMENT)' \
                        ')'
# 20
create_tblPropertyDocuments = 'CREATE TABLE IF NOT EXISTS "tblPropertyDocuments" (' \
                              '"propertyDocumentID"	INTEGER,' \
                              '"propertyDocumentAdditionalInfo"	TEXT,' \
                              '"propertyDocumentSapRegisterNo"	TEXT NOT NULL,' \
                              '"propertyDocumentSapRegistrationDate"	TEXT NOT NULL,' \
                              '"propertyDocumentType"	TEXT NOT NULL,' \
                              '"projectID"	INTEGER NOT NULL,' \
                              'PRIMARY KEY("propertyDocumentID")' \
                              ')'
# 21
create_tblStreets = 'CREATE TABLE IF NOT EXISTS "tblStreets" (' \
                    '"streetID"	INTEGER,' \
                    '"streetName"	TEXT NOT NULL,' \
                    'PRIMARY KEY("streetID" AUTOINCREMENT)' \
                    ')'
# 22
create_tblRegions = 'CREATE TABLE IF NOT EXISTS "tblRegions" (' \
                    '"regionId"	INTEGER,' \
                    '"regionName"	TEXT NOT NULL,' \
                    'PRIMARY KEY("regionId" AUTOINCREMENT)' \
                    ')'
# 23
create_tblPrecincts = 'CREATE TABLE IF NOT EXISTS "tblPrecincts" (' \
                      '"localizationPrecinct"	TEXT NOT NULL UNIQUE' \
                      ')'
# 24
create_tblPlaces = 'CREATE TABLE IF NOT EXISTS "tblPlaces" (' \
                   '"placeID"	INTEGER,' \
                   '"placeName"	TEXT NOT NULL,' \
                   'PRIMARY KEY("placeID" AUTOINCREMENT)' \
                   ')'
# 25
create_tblProjectManagers = 'CREATE TABLE IF NOT EXISTS "tblProjectManagers" (' \
                            '"Id"	INTEGER,' \
                            '"projectManager"	TEXT NOT NULL,' \
                            '"projectManagerPhone"	TEXT,' \
                            '"projectManagerMail"	TEXT,' \
                            'PRIMARY KEY("Id")' \
                            ')'
# 26
create_tblPSPelement = 'CREATE TABLE "tblPSPelement" (' \
                       '"elementID"	INTEGER,' \
                       '"elementValue"	TEXT NOT NULL UNIQUE,' \
                       'PRIMARY KEY("elementID" AUTOINCREMENT)' \
                       ')'
# 27
create_tblEmailTemplates = 'CREATE TABLE IF NOT EXISTS "tblEmailTemplates" (' \
                           '"templateID"	INTEGER,' \
                           '"templateName"	TEXT NOT NULL UNIQUE,' \
                           '"templateHeader"	NUMERIC NOT NULL UNIQUE,' \
                           '"templatePriority"	INTEGER NOT NULL,' \
                           '"templateDocRequest"	INTEGER NOT NULL,' \
                           '"templateRequestedDocName"	TEXT NOT NULL,' \
                           '"templateLexicalForms"	INTEGER NOT NULL,' \
                           '"templateLocalizationIsPointed"	INTEGER NOT NULL,' \
                           '"templateLandRegisterIsPointed"	INTEGER NOT NULL,' \
                           '"templateAnnexesIsPointed"	INTEGER NOT NULL,' \
                           'PRIMARY KEY("templateID" AUTOINCREMENT)' \
                           ')'
# 28
create_tblDocumentsTemplates = 'CREATE TABLE IF NOT EXISTS "tblDocumentsTemplates" (' \
                               '"documentTemplateID"	INTEGER,' \
                               '"documentTemplateName"	TEXT NOT NULL,' \
                               '"documentTemplateIsPointed"	INTEGER,' \
                               '"documentTemplateDescription"	TEXT NOT NULL,' \
                               '"documentType"	TEXT NOT NULL,' \
                               '"documentQuantity"	INTEGER,' \
                               '"documentAnnexesIsPointed"	INTEGER,' \
                               '"localizationIsPointed"	INTEGER,' \
                               '"documentAdditionalInfo"	TEXT,' \
                               '"localizationLandRegisterIsPointed"	INTEGER,' \
                               '"documentLexicalForms"	INTEGER,' \
                               'PRIMARY KEY("documentTemplateID" AUTOINCREMENT)' \
                               ')'

create_tblReports = 'CREATE TABLE "tblReports" (' \
                    '"reportID"	INTEGER,' \
                    '"reportName"	TEXT NOT NULL,' \
                    '"reportDefinition"	TEXT NOT NULL,' \
                    '"reportDescription"	TEXT NOT NULL,' \
                    '"reportOutput"	TEXT NOT NULL,' \
                    'PRIMARY KEY("reportID" AUTOINCREMENT)' \
                    ')'

create_tblToDo = 'CREATE TABLE "tblToDo" (' \
                 '"todoId"	INTEGER,' \
                 '"todoTaskCase"	INTEGER,' \
                 '"todoRegistrationDate"	TEXT NOT NULL,' \
                 '"todoItem"	TEXT NOT NULL,' \
                 '"todoDeadLine"	TEXT NOT NULL,' \
                 'PRIMARY KEY("todoId" AUTOINCREMENT)' \
                 ')'

create_view_main_report = '''CREATE VIEW main_report AS
SELECT tp.projectID as 'Teczka', 
tp.projectSegment as 'Segment', 
tp.projectSapNo as 'Numer', 
tp.projectInflow as 'Wpływ', 
tp.projectTask as 'Zadanie', 
tp.projectManager as 'Inżynier',
(SELECT GROUP_CONCAT('Dz. nr ' || tl.localizationPlotNo ||', AM-'|| tl.localizationMapNo  || ', Obr. '|| tl.localizationPrecinct || ', ' || tpl.placeName  ||'; ', '')
FROM tblLocalizations tl 
INNER JOIN tblPlaces tpl ON tpl.placeID = tl.placeName 
WHERE tl.projectID = tp.projectID 
GROUP BY tl.projectID) as 'Lokalizacja',
tl.ownerName as 'Podmiot',
ts.statusName as 'Status',
(SELECT GROUP_CONCAT(tr.regulationDocumentDate ||' '|| tr.regulationDocumentSignature || '; ', '')
FROM tblRegulations tr 
WHERE tr.projectID = tp.projectID 
GROUP BY tr.projectID) as 'Regulacja',
(SELECT GROUP_CONCAT(tpd.propertyDocumentType ||' nr '|| tpd.propertyDocumentSapRegisterNo || '; ', '')
FROM tblPropertyDocuments tpd 
WHERE tpd.projectID = tp.projectID 
GROUP BY tpd.projectID) as 'OT'
FROM tblProjects tp
INNER JOIN tblStatus ts ON ts.statusID = tp.statusName
INNER JOIN tblLocalizations tl ON tl.projectID = tp.projectID
LEFT JOIN tblRegulations tr ON tr.projectID = tp.projectID 
LEFT JOIN tblPropertyDocuments tpd ON tpd.projectID = tp.projectID 
GROUP BY tp.projectID
ORDER BY tp.projectID'''

main_report = '''SELECT Teczka as 'Teczka', 
Segment as 'Segment', 
Numer as 'Numer', 
Wpływ as 'Wpływ', 
Zadanie as 'Zadanie', 
Inżynier as 'Inżynier', 
Lokalizacja as 'Lokalizacja', 
Podmiot as 'Podmiot',
Status as 'Status',
Regulacja as 'Regulacja',
OT as 'OT'
FROM main_report'''

actions_to_observe = '''SELECT projectID as 'Teczka', 
actionDate as 'Data', 
actionDescription as 'Czynność' 
FROM tblActions 
WHERE actionKeepAttention > 0 
GROUP BY projectID, actionDate  
ORDER BY actionDate
'''