#!/bin/python
#
# Author: Thanh Nguyen
# Description: sleep sort algorithm
#
import sys
import time
import multiprocessing as mtp


def sleep_and_print(num):
    """ Sleep num seconds, then print that number
    """
    time.sleep(int(num))
    print "%d " % int(num),


def value_is_int(value):
    """ Check a value is a int or not
    """
    try:
        intVal = int(value)
        return True
    except:
        return False

if  __name__ == "__main__":
    if len(sys.argv) < 2:
        print "ERROR, you need provide some integer number" \
            " as arguments"
        sys.exit(1)

    nums = sys.argv[1:]
    for num in nums:
        if not value_is_int(num):
            print "ERROR, all arguments must be the integer"
            sys.exit(1)
        else:
            p = mtp.Process(target=sleep_and_print, args=(num, ))
            p.start()
