#!/usr/bin/python -tt
# skvidal@fedoraproject.org, modified by David Laval
# gplv2+

## XMPP notification
#define command{
#    command_name    notify-host-by-xmpp
#    command_line    $PLUGINSDIR$/notify_by_xmpp.py -a $PLUGINSDIR$/notify_by_xmpp.ini "Host '$HOSTALIAS$' is $HOSTSTATE$ - Info : $HOSTOUTPUT$" $CONTACTEMAIL$
#}
#
#define command{
#    command_name    notify-service-by-xmpp
#    command_line    $PLUGINSDIR$/notify_by_xmpp.py -a $PLUGINSDIR$/notify_by_xmpp.ini "$NOTIFICATIONTYPE$ $HOSTNAME$ $SERVICED ESC$ $SERVICESTATE$ $SERVICEOUTPUT$ $LONGDATETIME$" $CONTACTEMAIL$
#}

# needs a config file to get username/pass/other info format is:

#[xmpp_account]
#server=xxmp.vccloud.vn
#port=5222
#username=yourusername
#password=yourpasssword
#resource=monitoring

defaults = {'server':'xmpp.vccloud.vn',
            'port': 5222,
            'resource':'monitoring'}

# until xmppony is inplace

import warnings
warnings.simplefilter("ignore")

import xmpp
from xmpp.protocol import Message


from optparse import OptionParser
import ConfigParser
import sys
import os
import logging
import time

logging.basicConfig(filename="/var/log/shinken/xmpp.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)

msgid = time.time()
time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(msgid))

parser = OptionParser()
parser.add_option("-a", dest="authfile", default=None, help="file to retrieve username/password/server/port/resource information from")
opts, args = parser.parse_args()

conf = ConfigParser.ConfigParser(defaults=defaults)
if not opts.authfile or not os.path.exists(opts.authfile):
    logger.error("<%s> no config/auth file specified, can't continue" % time_str)
    print "<%s> no config/auth file specified, can't continue" % time_str
    sys.exit(1)

conf.read(opts.authfile)
if not conf.has_section('xmpp_account') or not conf.has_option('xmpp_account', 'username') or not conf.has_option('xmpp_account', 'password'):
    logger.error("<%s> cannot find at least one of: config section 'xmpp_account' or username or password" % time_str)
    print "<%s> cannot find at least one of: config section 'xmpp_account' or username or password" % time_str
    sys.exit(1)
server = conf.get('xmpp_account', 'server')
username = conf.get('xmpp_account', 'username')
password = conf.get('xmpp_account', 'password')
resource = conf.get('xmpp_account', 'resource')
port = conf.get('xmpp_account', 'port')


if len(args) < 1:
    logger.error("<%s> xmppsend message [to whom, multiple args]" % time_str)
    print "<%s> xmppsend message [to whom, multiple args]" % time_str
    sys.exit(1)

msg = args[0]

msg = msg.replace('\\n', '\n')
domainsv = server.split('.',1)[1]
c = xmpp.Client(domainsv)

con  = c.connect(server = (server, port))
if not con:
    logger.error("<%s>Error: could not connect to server: %s:%s" % (time_str, server, port))
    print "<%s> Error: could not connect to server: %s:%s" % (time_str, server, port)
    sys.exit(1)

auth = c.auth(user=username, password=password, resource=resource)
if not auth:
    logger.error("<%s> Error: Could not authenticate to server: %s:%s" % (time_str, server, port))
    print "<%s> Error: Could not authenticate to server: %s:%s" % (time_str, server, port)
    sys.exit(1)


if len(args) < 2:
    r = c.getRoster()
    for user in r.keys():
        if user == username:
            continue
        logger.info(("<%s> send xmpp message to %s" % (time_str, user)))
        c.send(Message(user, '%s' % msg))
else:
    for user in args[1:]:
        logger.info(("<%s> send xmpp message to %s" % (time_str, user)))
        c.send(Message(user, '%s' % msg))
    
