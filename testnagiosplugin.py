import nagiosplugin
import commands
import re
import argparse


class TestNagios(nagiosplugin.Resource):
    def get_value(self):
        status, output = commands.getstatusoutput("\
                         df -h | awk 'NR==2' | \
                         grep -o '[0-9\.]*' | awk 'NR==2'\
                         ")
        value = float(output)
        return value

    def probe(self):
        value = self.get_value()
        return [nagiosplugin.Metric('test_nagios', value)]


def main():
    argp = argparse.ArgumentParser(description=__doc__)
    argp.add_argument('-w', '--warning', metavar='RANGE', default='',
                      help='return warning if load is outside RANGE')
    argp.add_argument('-c', '--critical', metavar='RANGE', default='',
                      help='return critical if load is outside RANGE')
    args = argp.parse_args()
    check = nagiosplugin.Check(
        TestNagios(),
        nagiosplugin.ScalarContext('test_nagios', args.warning, args.critical))
    check.main()

if __name__ == '__main__':
    main()
