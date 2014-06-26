from optparse import OptionParser
import sys
import os

# Parse commandline options:
parser = OptionParser(usage="%prog -w <warning threshold> -c <critical threshold> [ -h ]")
parser.add_option("-w", "--warning",
    action="store", type="string", dest="warn_threshold", help="Warning threshold is decimal numbere")
parser.add_option("-c", "--critical",
    action="store", type="string", dest="crit_threshold", help="Critical threshold is decimal numbere")
(options, args) = parser.parse_args()


def check_server_load():
    if not options.crit_threshold:
        print "UNKNOWN: Missing critical threshold value."
        sys.exit(3)
    if not options.warn_threshold:
        print "UNKNOWN: Missing warning threshold value."
        sys.exit(3)
    if float(options.crit_threshold) <= float(options.warn_threshold):
        print "UNKNOWN: Critical percentage can't be equal to or bigger than warning percentage."
        sys.exit(3)
    exsp = os.popen(" w | head -n 1 | awk '{print $(NF-2),$(NF-1),$NF}' | tr -d ','").readline().strip().split(" ")
    
    for value in exsp:
        if float(value) >= float(options.crit_threshold):
            print "CRITICAL: load average: %s, %s, %s" % (exsp[0], exsp[1], exsp[2])
            sys.exit(2)
    if float(value) >= float(options.warn_threshold):
        print "WARNING: load average: %s, %s, %s" % (exsp[0], exsp[1], exsp[2])
        sys.exit(1)
    else:
        print "OK: load average: %s, %s, %s" % (exsp[0], exsp[1], exsp[2])
        sys.exit(0)

if __name__ == '__main__':
    check_server_load()