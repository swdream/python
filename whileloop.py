correctpassword = 'thanhnt'
while True:
    password = raw_input("enter your password:")
    if password == correctpassword:
        print 'you logined'
        break
    print 'enter your password again!'