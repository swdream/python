import time

def tail_F(filename):
    p = 0
    with open(filename, 'r') as f:
        while True:
            f.seek(p)
            new_line = f.read()
            p = f.tell()
            if new_line:
                print new_line
                print str(p).center(10).center(80, '=')
            # while True is disaster, see you top on how this use CPU.
            time.sleep(1)

if __name__ == '__main__':
    filename = 'whileloop.py'
    tail_F(filename)