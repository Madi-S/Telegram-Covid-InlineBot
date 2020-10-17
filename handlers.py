import logging
import logging.handlers
import smtplib
from os import environ


class BufferingSMTPHandler(logging.handlers.BufferingHandler):
    def __init__(self):
        logging.handlers.BufferingHandler.__init__(self, 5)
        self.mailhost = 'smtp.gmail.com'
        self.mailport = 465
        self.fromaddr = environ['SMTP_EMAIL']
        self.toaddr = 'shaiken.m@mail.ru'
        self.password = environ['SMTP_PASSWORD']
        self.toaddrs = environ['SMTP_EMAIL']
        self.subject = 'LOG FROM TELEGRAM BOT'

        self.setFormatter(logging.Formatter(
            '{levelname} - {asctime} - {lineno} - {name} -  In {funcName}: {message}', style='{'))

    def flush(self):
        if len(self.buffer) > 0:
            with smtplib.SMTP_SSL(self.mailhost, self.mailport) as smtp:
                smtp.login(self.fromaddr, self.password)

                subject = self.subject
                body = 'CRITICAL LOGS FROM TELEGRAM BOT:\n\n'

                for record in self.buffer:
                    record = self.format(record) + '\n'
                    body += record

                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(self.fromaddr, self.toaddr, msg)
