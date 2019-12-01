import yagmail
# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']
def get_email(send_text,subject_text):
    # 发邮件
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="xxx@.com", password="授权码", host='smtp.qq.com')
    subject = subject_text + '核对不上,请核查'
    # 发送邮件
    yag.send('yj624@foxmail.com', subject, send_text)

get_email(contents)