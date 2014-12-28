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
    time.sleep(num)
    print "%d " % num,


if  __name__ == "__main__":
    if len(sys.argv) < 2:
        print "ERROR, you need provide some integer number" \
            " as arguments"
        sys.exit(1)

    nums = sys.argv[1:]
    try:
        for num in nums:
            p = mtp.Process(target=sleep_and_print, args=(int(num), ))
            p.start()
    except Exception as e:
        print "ERROR, %s" % e
