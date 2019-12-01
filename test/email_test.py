# smtplib模块负责连接服务器和发送邮件
# MIMEText：定义邮件的文字数据
# MIMEImage：定义邮件的图片数据
# MIMEMultipart：负责将文字图片音频组装在一起添加附件

import smtplib

from email.mime.text import MIMEText
from subprocess import Popen, PIPE
# import commands


def send_mail(sender, recevier, subject, html_content):
    msg = MIMEText(html_content, 'html', 'utf-8')
    msg["From"] = sender
    msg["To"] = recevier
    msg["Subject"] = subject
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())


send_mail("sender@xxxx.com", "1424194274@qq.com", "linux python 邮件测试", "yj mail_text")
# send_mail("sender@xxxx.com", "1424194274@qq.com,receive2@xxxx.com", "linux python 邮件测试", "yj mail_text")
