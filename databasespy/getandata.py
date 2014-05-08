import MySQLdb
import json

from MySQLdb import cursors

# Open database connection
db = MySQLdb.connect("localhost","root","xxxxx","birthday")

# prepare a cursor object using cursor() method
cursor = db.cursor(cursors.SSCursor)

# Drop table if it already exist using execute() method.
cursor.execute("select fullname, birthday, gmail from birthday_9a1")
data = cursor.fetchall()
dict_row = []
for row in data:
    t = (row[0], row[1], row[2])
    dict_row.append(t)

print dict_row
#print len(dict_row)
#for i in range(len(dict_row)):
#    d = {dict_row[i][0]:{"birthday":str(dict_row[i][1]),'email':str(dict_row[i][2])}}
#
#print d
for i in range(2):
    print dict_row[i][1]

cursor.close()