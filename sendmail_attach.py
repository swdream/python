import smtplib
import logging

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

username = "ngtthanh1010@gmail.com"
password = "xxxxxxx"

msg = MIMEMultipart('relate')


def attach_text_file(filename):
    try:
        logger.info('openning file %s' % filename)
        with open(filename, 'rb') as ftext:
            msgtext = MIMEText(ftext.read(), 'text')
            msgtext.add_header("Content-ID", "<text1>")
            msgtext.add_header("Content-Disposition",
                               "attachment", filename=filename)
            msgtext.add_header("Content-Disposition",
                               "inline", filename=filename)
            msg.attach(msgtext)
    except Exception as e:
        logger.error(e, exc_info=True)


def attach_img(img):
    try:
        logger.info('openning file %s' % img)
        with open(img, 'rb') as fimage:
            msgimg = MIMEImage(fimage.read(), 'png')
            msgimg.add_header("Content-ID", "<image1>")
            msgimg.add_header("Content-Disposition", "attachment",
                              filename=img)
            msgimg.add_header("Content-Disposition", "inline",
                              filename=img)
            msg.attach(msgimg)
    except Exception as e:
        logger.error(e, exc_info=True)


def send_mail(rctps, subject, body, textfile=None, img=None):
    str_all_mails = ', '.join(rctps)

    if textfile is None and img is None:
        return None

    time_str  = str(datetime.now())

    msg["From"]    = 'ngtthanh1010@gmail.com'
    msg["To"]      = str_all_mails
    msg["Subject"] = subject
    body = MIMEText(body, 'plain')

    if img is not None and textfile is not None:
        attach_text_file(textfile)
        attach_img(img)

    if img is None:
        attach_text_file(textfile)

    if textfile is None:
        attach_img(img)

    msg.attach(body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        logger.info('%s login on mail server' % time_str )
        server.login(username, password)
        logger.info('%s logged on mail server' % time_str )
        logger.info('%s sending mail to %s' % (time_str, str_all_mails))
        server.sendmail(username, rctps, msg.as_string())
        logger.info ('%s sent mail sucessful' % time_str)
        server.quit()
    except Exception as e:
        logger.error(e, exc_info=True)


if __name__ == '__main__':
    rctps = ["ngtthanh1010@gmail.com"]
    subject = 'Test'
    body  = "My test email"
    filename = "hehe.txt"
    imgfile ="Screenshot from 2014-07-11 09:29:20.png"
    send_mail(rctps, subject, body, textfile=filename)
#    send_mail(rctps, subject, body, textfile=None, img=imgfile)
#    send_mail(rctps, subject, body, textfile=filename, img=imgfile)
