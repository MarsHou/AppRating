#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


class DataSend(object):
    def __init__(self):
        self.smtp_server = ''
        self.from_address = ''
        self.password = ''
        self.to_addresses = ['']

    def send_email(self, file_name):
        msg = MIMEMultipart()
        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_address, self.password)
        server.sendmail(self.from_address, self.to_addresses, msg.as_string())
        server.quit()
