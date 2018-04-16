import smtplib 
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def sendmail(smtp, port, usrname, passwd, rcptto, text):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header('UpdateIP automatic mail'.decode('utf-8')).encode()
    msg['From'] = usrname
    msg['To'] = rcptto
    msg['Reply-to'] = usrname
    msg['Message-id'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate() 
    textplain = MIMEText(text, _subtype='plain', _charset='UTF-8')
    msg.attach(textplain)

    server = smtplib.SMTP_SSL(smtp, int(port))
    server.login(usrname, passwd)

    server.sendmail(usrname, rcptto, msg.as_string())
    server.quit()