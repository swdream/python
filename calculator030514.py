import argparse

def main():
    parser = argparse.ArgumentParser(description='Calculate two input number')
    parser.add_argument(
        'first', metavar='int', type = int,
        help = 'first number'
    )
    parser.add_argument(
        'second', metavar='int', type= int,
        help = 'second number'
    )
    parser.add_argument(
        'oper', metavar= 'oper', type = str,
        help = 'operator +, - or *'
    )

    args = parser.parse_args()

    first = int(args.first)
    second = int(args.second)
    oper = args.oper


    res = ''

    if oper == '+':
        res = first + second

    if oper == '-':
        res = first - second

    if oper == '*':
        res = first * second

    else:
        print ' not supported'

    print res

if __name__ == '__main__':
    main()