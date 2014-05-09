import os
import sys
import urllib
import datetime
import smtplib
import logging
import graphitesend


from ConfigParser import SafeConfigParser


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


parser = SafeConfigParser()
log.info('Reading config file')
parser.read('downcheck.conf')
stdtime = parser.get('download', 'stdtime')
servermail = parser.get('email-info', 'servermail')
username = parser.get('email-info', 'username')
password = parser.get('email-info', 'password')
rctps = parser.get('email-info', 'recipients').split(',')


def send_mail(subject, body):
    str_all_mails = ', '.join(rctps)
    headers = ["From: " + username,
               "Subject: " + subject,
               "To: " + str_all_mails,
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    server = smtplib.SMTP(servermail)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr=username, to_addrs=rctps,
    msg=(headers + "\r\n\r\n" + body))
    log.info('Sent mail %r to %s', subject, str_all_mails)
    server.quit()


def down_packages(url):
    log.info('downloading a package')
    testpakge = urllib.URLopener()
    testpakge.retrieve(url, 'downcheck')
    return None


def send_metric(waittime):
    g = graphitesend.init(graphite_server='xxx', graphite_port=2003, system_name='checkdownload')
    try:
        g.send('time', waittime)
        log.info(' sent data to graphite server')
    except(TypeError, GraphiteSendException) as e:
        log.error('can not send data to graphite server')


def check_timeout(url):
    startTime = datetime.datetime.now()
    try:
        down_packages(url)
    except Exception as e:
        log.error(e, exc_info=True)
        return None

    now = datetime.datetime.now()
    waittime = now - startTime
    timeerror = 2.0 * float(float(stdtime))
    if float(waittime.total_seconds()) > timeerror:
        subject = ('download time is greater than the normal time: %r > %r'
                 %(waittime.total_seconds(), stdtime))
        log.info('subject: %r' % subject)
        body = ("Download time is greater than 2.0 times the normal time - \n"
                "Download time:%r seconds - \n"
                "Nomal download time: %r seconds"
                % (waittime.total_seconds(), stdtime))

        log.info('body: %r' % body)
        try:
            log.info('sending email')
            send_mail(subject, body)
            send_metric(waittime.total_seconds())
        except Exception as e:
            log.error(e, exc_info=True)
            return None

    else:
        log.info('downloaded package susscessful')
        subject = ('downloaded package susscessful, download time: %f seconds'
                   % waittime.total_seconds())
        log.info('subject: %r' % subject)
        body = ("Download time is allowed - \n"
                "Download time:%r seconds - \n"
                "Nomal download time: %r seconds"
                % (waittime.total_seconds(), stdtime))

        log.info('body: %r' % body)
        try:
            log.info('sending email')
            send_mail(subject, body)
            send_metric(waittime.total_seconds())
        except Exception as e:
            log.error(e, exc_info=True)
            return None


if __name__ == '__main__':
    url = parser.get('download', 'url')
    check_timeout(url)
