import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '15161737044@163.com'
msg['to'] = '1627697510@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('15161737044@163.com', 'xh177151')
smtp.sendmail('15161737044@163.com', '1627697510@qq.com', str(msg))
smtp.quit()