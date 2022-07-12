import email
import smtplib
import imaplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class Mail:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, recipients: list, subject: str = None, message: str = None, header: str = None):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        try:
            ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
            ms.ehlo()
            ms.starttls()
            ms.ehlo()
            try:
                ms.login(self.login, self.password)
            except:
                raise Exception('Ошибка авторизации')
            ms.sendmail(self.login, recipients, msg.as_string())
            ms.quit()
        except:
            raise Exception('Ошибка сервера')

    def recieve_message(self, header: str = None):
        try:
            mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
            try:
                mail.login(self.login, self.password)
            except:
                raise Exception('Ошибка авторизации')
            mail.list()
            mail.select("inbox")
            try:
                criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
                result, data = mail.uid('search', None, criterion)
                assert data[0], 'There are no letters with current header'
                latest_email_uid = data[0].split()[-1]
                result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)
                mail.logout()
                return email_message
            except:
                print(f'Писем с заголовком {header} нет')
        except:
            raise Exception('Ошибка сервера')


if __name__ == '__main__':
    recipients = ['olegnsksib@gmail.com']
    subject = 'Subject'
    message = 'Test_message'

    mail_google = Mail(config.login, config.password)
    mail_google.send_message(recipients, "Тестовая тема письма", 'Тестовый текст письма')
    last_message = mail_google.recieve_message()
