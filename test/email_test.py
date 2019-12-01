# smtplib模块负责连接服务器和发送邮件
# MIMEText：定义邮件的文字数据
# MIMEImage：定义邮件的图片数据
# MIMEMultipart：负责将文字图片音频组装在一起添加附件

import smtplib

# from email.mime.text import MIMEText
# from subprocess import Popen, PIPE
# # import commands
#
#
# def send_mail(sender, recevier, subject, html_content):
#     msg = MIMEText(html_content, 'html', 'utf-8')
#     msg["From"] = sender
#     msg["To"] = recevier
#     msg["Subject"] = subject
#     p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
#     p.communicate(msg.as_string())
#
#
# send_mail("sender@xxxx.com", "1424194274@qq.com", "linux python 邮件测试", "yj mail_text")
# send_mail("sender@xxxx.com", "1424194274@qq.com,receive2@xxxx.com", "linux python 邮件测试", "yj mail_text")

# -------------------------------------------------------------------------

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'from@runoob.com'
# receivers = ['1424194274@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
# message['To'] = Header("1424194274@qq.com", 'utf-8')  # 接收者
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")

# --------------------------------------------
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# import smtplib
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr(( \
#         Header(name, 'utf-8').encode(), \
#         addr.encode('utf-8') if isinstance(addr, unicode) else addr))
#
# from_addr = raw_input('From: ')
# password = raw_input('Password: ')
# to_addr = raw_input('To: ')
# smtp_server = raw_input('SMTP server: ')
#
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# ---------------------------------------------------

import yagmail

#链接邮箱服务器
yag = yagmail.SMTP( user="1424194274@qq.com", password="yinjun121927", host='smtp.qq.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']

# 发送邮件
yag.send('yj624@foxmail.com', 'python邮件测试', contents)
