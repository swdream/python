from datetime import datetime
from datetime import date
# Isocalendar()
# print out a 3-tuple( ISO year, ISO week number, ISO weekday)
today = datetime.today()
print today.isocalendar()

# weekday()
# print out the day of the week as a integer number, where monday is 0, sunday is 6
print today.weekday()

# check a day:
if today.date()==date(2014,5,4):
    print 'today is %s' today

# check today is monday
if today.weekday()==0:
   blabla


