#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import exists
import re


class Email:

    def __init__(self,
                 sender: str,
                 receiver: [str, list],
                 title: str,
                 server: str,
                 auth_code: str,
                 message: str = None,
                 attachment_file: [str, list] = None):
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.message = message
        self.attachment_file = attachment_file
        self.server = server
        self.auth_code = auth_code

        self.msg = MIMEMultipart('related')

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['Form'] = self.sender
        self.msg['To'] = self.receiver

        if self.message:
            self.msg.attach(MIMEText(self.message, 'plain', 'utf-8'))

        if self.attachment_file:
            if isinstance(self.attachment_file, str):
                self._attach_file(self.attachment_file)
            if isinstance(self.attachment_file, list):
                for _path in self.attachment_file:
                    self._attach_file(_path)

        try:
            smtp_server = smtplib.SMTP(self.server)
            smtp_server.login(self.sender, self.auth_code)
            smtp_server.sendmail(self.sender, self.receiver, self.msg.as_string())
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


mail = Email(sender='1462367817@qq.com',
             receiver='1462367817@qq.com',
             title='title',
             server='smtp.qq.com',
             auth_code='hivwbxkuautfifji',
             message='ttt',
             attachment_file=r'D:\Tools\git\workspace\Interface_project\chapter7\generator.py')
# mail.send()
