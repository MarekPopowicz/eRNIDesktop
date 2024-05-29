import win32com.client as win32
from utils import info_boxes


# Drafting and sending email notification to senders. You can add other senders' email in the list
def send_notification(mail, subject, body, path, attachments, priority=False):
    outlook = win32.Dispatch('outlook.application')
    olFormatHTML = 2
    olFormatPlain = 1
    olFormatRichText = 3
    olFormatUnspecified = 0
    olMailItem = 0x0

    newMail = outlook.CreateItem(olMailItem)
    newMail.Subject = subject
    newMail.BodyFormat = olFormatPlain  # or olFormatRichText or olFormatPlain or olFormatHTML
    # newMail.HTMLBody = "test"
    newMail.Body = body
    newMail.To = mail
    if priority:
        newMail.Importance = 2
    else:
        newMail.Importance = 0
    # newMail.CC = 'xyz@gmail.com'

    flag = False
    if len(attachments) > 0:
        for attachment in attachments:
            if attachment == '':
                flag = True
                continue
            a = path + '\\' + attachment
            newMail.Attachments.Add(a)
    if flag:
        info_boxes.warningBox('Brak załącznika', 'Nie wszystkie załączniki z listy zostały dołączone')
    newMail.display()
    # or just use this instead of .display() if you want to send immediately
    # newMail.Send()