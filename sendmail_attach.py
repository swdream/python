import smtplib
import logging
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

logging.basicConfig(level=logging.DEBUG)
my_logger = logging.getLogger(__name__)

def send_mail(efrom, eto, subject, body, filename):
    msgid = time.time()
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',
                             time.localtime(msgid))

    username = "ngtthanh1010"
    password = "xxxxx"
    body = body
    #textfile = "textattach.txt"
    imfile   = "imattach.png"
 
    msg = MIMEMultipart('relate')
    msg["From"]    = efrom
    msg["To"]      = eto
    msg["Subject"] = subject
    msgtalk = MIMEText(body, 'plain')
 
    #ftext = open(textfile, 'rb')
    #msgtext = MIMEText(ftext.read(), 'text')
    #msgtext.add_header("Content-ID", "<text1>")
    #msgtext.add_header("Content-Disposition",
    #                   "attachment", filename=textfile)
    #msgtext.add_header("Content-Disposition",
    #                   "inline", filename=textfile)

    fimage = open(filename, 'rb')
    msgim = MIMEImage(fimage.read(), 'png')
    msgim.add_header("Content-ID", "<image1>")
    msgim.add_header("Content-Disposition", "attachment",
                     filename=filename)
    msgim.add_header("Content-Disposition", "inline",
                     filename=filename)
    msg.attach(msgtalk)
    #msg.attach(msgtext)
    msg.attach(msgim)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.ehlo()
        server.starttls()
        #server.ehlo()
        my_logger.info('%s login on mail server' % time_str )
        server.login(username, password)
        my_logger.info('%s logged on mail server' % time_str )
        my_logger.info('%s sending mail to %s' % (time_str, eto ))
        server.sendmail(efrom, eto, msg.as_string())
        my_logger.info ('%s sent mail sucessful' % time_str)
        server.quit()
    except Exception as e:
        my_logger.error(e, exc_info=True)

if __name__ == '__main__':
    efrom = "ngtthanh1010@gmail.com"
    eto   = "xxxxx"
    subject = 'Test'
    body  = "My test email"
    filename = "xxxxx"
    send_mail(efrom, eto, subject, body, filename)
