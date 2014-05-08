# get data from a sql database
# a databae named thanhnt created
# a table named address created in thanhnt database

import MySQLdb

def get_data(databasename, tablename):
    # open database connection
    connection = MySQLdb.connect(host="localhost",user="root", passwd="xxx", db='%s' % databasename)
    #
    cursor = connection.cursor()
    cursor.execute("select * from %s" % tablename)
    data = cursor.fetchall()
    print data
    # use fetchone() if want to get a row
    for row in data:
        print row,
        print ''.join(str(item)+ ', ' for item in row)
        # print row[i]
if __name__ == '__main__':
    databasename = 'thanhnt'
    tablename = 'address'
    try:
        get_data( databasename, tablename)
    except Exception as e:
        print 'can not access %s db' % databasename
