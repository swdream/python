import logging
import os
import urllib
from functools import wraps
import errno
import signal
import sys
import datetime

from sys import argv


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


_script, normal_time, url = argv
log.info('normal time: %r seconds' % normal_time)
normal_time = float(normal_time)
timeerror = 1.5 * normal_time
log.info('timeerror: %r seconds' % timeerror)

class timeout(object):

    def __init__(self, seconds=60, error_message=os.strerror(errno.ETIME)):
        self.seconds = seconds
        self.message = error_message

    def _handle_timeout(self, *args, **kwargs):
        log.error("Error: Connection time out")
        sys.exit(1)

    def __call__(self, func):

        def wrapped_f(*args, **kwargs):
            signal.signal(signal.SIGALRM, self._handle_timeout)
            signal.alarm(self.seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapped_f


def down_packages(url):
    log.info('downloading a package')
    startTime = datetime.datetime.now()
    testpakge = urllib.URLopener()
    testpakge.retrieve(url, 'downcheck')
    now = datetime.datetime.now()
    downtime = now - startTime
    log.info('Download time: %r seconds' %downtime.total_seconds())

@timeout(int(timeerror))
def check_timeout(url):
    down_packages(url)

if __name__ == '__main__':
    check_timeout(url)
