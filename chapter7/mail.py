#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import exists
import re
from setting import *


class Email:

    def __init__(self,
                 message: str = None,
                 attachment_file: [str, list] = None):
        self.message = message
        self.attachment_file = attachment_file

        self.msg = MIMEMultipart('related')

    def send(self):

        self.msg['Subject'] = title
        self.msg['From'] = sender
        self.msg['To'] = ','.join(receiver)

        if self.message:
            self.msg.attach(MIMEText(self.message, 'plain', 'utf-8'))

        if self.attachment_file:
            if isinstance(self.attachment_file, str):
                self._attach_file(self.attachment_file)
            if isinstance(self.attachment_file, list):
                for _path in self.attachment_file:
                    self._attach_file(_path)

        try:
            smtp_server = smtplib.SMTP(server)
            smtp_server.login(sender, auth_code)
            smtp_server.sendmail(sender, receiver, self.msg.as_string())
            smtp_server.quit()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('Error: 无法发送邮件')

    def _attach_file(self, file_path):
        if not exists(file_path):
            raise FileNotFoundError(f'{file_path}:附件文件不存在或者附件文件路径错误')
        with open(file_path, 'r', encoding='utf-8') as f:
            att = MIMEText(f.read(), 'plain', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            file_name = re.split(r'[\\|/]', file_path)[-1]
            att['Content-Disposition'] = f'attachment; filename={file_name}'
            self.msg.attach(att)


# mail = Email(message='ttt', attachment_file=r'D:\Tools\git\workspace\Interface_project\chapter7\generator.py')
# mail.send()
