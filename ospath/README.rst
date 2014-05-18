Os.path- thao tác với tên tệp tin
=====================

http://pymotw.com/2/ospath/

Os.path module có một vai trò rất lớn trong việc tạo ra cũng như phân tích, tạo sự đáng tin cậy cho filename

Parsing paths
----------------

Vấn đề đầu tiên là việc os.path có thể được sử dụng để phân tích các strings đại diện cho filename thành các thành phần cấu thành nên chúng.
Parsing path phụ thuộc vào một sô biến được định nghĩa trong os:
      - Os.sep: phân cách giữa các thành phần của path. ví dụ như "/", "\"
      - Os.extsep: phân cách giữa các filename  và thành phần mở rộng. Ví dụ : "."
      - Os.pardir: thành phần của path, là thư mục chứa filename đó
      - Os.curdir: thành phần của path, là thư mục hiện hành

split(): chuyển path thành hai thành phần riêng biệt, return lại một tupple
basename(): return lại thành phần thứ 2 của split()
dirname(): return lại thành phần thứ nhâts của split()
splitext() làm việc như split() nhưng nó return lại một tupple gồm hai phần, được phân cách bởi extsep
commonprefix(): nhận một list các path, và return lại phần chung của các path đó


Building paths
-----------------

+ Join(): kết hợp các thành phần path riêng
+ expanduser(): chuyển đổi kí tự ~ thành home directory::
             import os.path

             for user in [ '', 'dhellmann', 'postgres' ]:
                 lookup = '~' + user
                 print lookup, ':', os.path.expanduser(lookup)

kết quả hiển thị::
        $ python ospath_expanduser.py

        ~ : /Users/dhellmann
        ~dhellmann : /Users/dhellmann
        ~postgres : /Library/PostgreSQL/9.0


+ expandvars: mở rộng bất kì  biến shell environments trong đường dẫn::

        import os

        os.environ['MYVAR']= THANHNT
        print os.path.expandvars('path/to/$MYVAR')

kết quả hiển thị::

        path/to/THANHNT


Chuẩn hóa path
---------------

Sử dụng normpath()
Để convert một filename tương đối thành một file name tuyệt đối, có thể sử dụng abspath()::

      import os.path

      for path in [ '.', '..', './one/two/three', '../one/two/three']:
          print '"%s" : "%s"' % (path, os.path.abspath(path))

kết quả::

      "." : "/home/thanhnguyen/github/python/ospath"
      ".." : "/home/thanhnguyen/github/python"
      "./one/two/three" : "/home/thanhnguyen/github/python/ospath/one/two/three"
      "../one/two/three" : "/home/thanhnguyen/github/python/one/two/three"



File times
-------------------
Os.path cũng có thể được dùng để đưa ra thông tin về file khi nó kết hợp với time module::
      import os.path
      import time

      print 'File         :', __file__
      print 'Access time  :', time.ctime(os.path.getatime(__file__))
      print 'Modified time:', time.ctime(os.path.getmtime(__file__))
      print 'Change time  :', time.ctime(os.path.getctime(__file__))
      print 'Size         :', os.path.getsize(__file__)

kết quả::

      File         : ospath.py
      Access time  : Sun May 18 22:37:10 2014
      Modified time: Sun May 18 22:37:07 2014
      Change time  : Sun May 18 22:37:07 2014
      Size         : 824



Test file
---------------

Dùng để test các trường hợp xảy ra với một file::

      import os.path

      for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
          print 'File        :', file
          print 'Absolute    :', os.path.isabs(file)
          print 'Is File?    :', os.path.isfile(file)
          print 'Is Dir?     :', os.path.isdir(file)
          print 'Is Link?    :', os.path.islink(file)
          print 'Mountpoint? :', os.path.ismount(file)
          print 'Exists?     :', os.path.exists(file)
          print 'Link Exists?:', os.path.lexists(file)



Traversing a Directory Tree::
--------------------------



