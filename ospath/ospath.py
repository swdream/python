import os
import os.path


print __file__
print file
print os.path.dirname(__file__)

paths = ['home/thanhnt/file1.cfg',
		 'home/thanhnt/file/',
		 '/',
		 '.',
		 ''
]

for path in paths:
	print ("%s: %s" % (path, os.path.split(path)))


dirs = '/home/thanhnt/'
filename = 'thanhnt.cfg'
print os.path.join(dirs,filename)


for user in ['', 'dhellmann', 'postgres']:
	dirs = '~' + user
	#  converts the tilde (~) character to a user’s home directory.
	print dirs,':',os.path.expanduser(dirs)


for path in [ '.', '..', './one/two/three', '../one/two/three']:
    # convert a relative path to a complete absolute filename, use abspath()
    print '"%s" : "%s"' % (path, os.path.abspath(path))

import time

print 'File         :', __file__
print 'Access time  :', time.ctime(os.path.getatime(__file__))
print 'Modified time:', time.ctime(os.path.getmtime(__file__))
print 'Change time  :', time.ctime(os.path.getctime(__file__))
print 'Size         :', os.path.getsize(__file__)

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print 'File        :', file
    print 'Absolute    :', os.path.isabs(file)
    print 'Is File?    :', os.path.isfile(file)
    print 'Is Dir?     :', os.path.isdir(file)
    print 'Is Link?    :', os.path.islink(file)
    print 'Mountpoint? :', os.path.ismount(file)
    print 'Exists?     :', os.path.exists(file)
    print 'Link Exists?:', os.path.lexists(file)
