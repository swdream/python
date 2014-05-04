def arg_test(*args):
    for i in enumerate(args):
        print i, repr(args)

arg_test('haha', 1, [])