#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


class DataSend(object):
    def __init__(self):
        self.smtp_server = 'smtp.exmail.qq.com'
        self.from_address = ''
        self.password = ''
        self.to_addresses = ['']

    def send_email(self, sort_by, file_name):
        msg = MIMEMultipart()
        msg['From'] = Header('Mars', 'utf-8')
        msg['To'] = Header('Receiver', 'utf-8')
        msg['Subject'] = Header('Email Subject test', 'utf-8')

        # Email content
        content_msg = r'''<p> Crawl data Success by %s of sort </p>
        </br>
        <p>Attachment name: %s</p>''' % (sort_by, file_name)
        msg.attach(MIMEText(content_msg, 'html', 'utf-8'))
        # Email attachment
        att1 = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        att1['Content-Disposition'] = 'attachment; filename="%s"' % file_name
        msg.attach(att1)

        try:
            server = smtplib.SMTP(self.smtp_server, 25)
            server.set_debuglevel(1)
            server.login(self.from_address, self.password)
            server.sendmail(self.from_address, self.to_addresses, msg.as_string())
            server.quit()
            print('Send Email Success...')
        except smtplib.SMTPException:
            print('Error: Send Email Error...')
