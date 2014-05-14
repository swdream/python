import datetime

def get_file_name():
    to_day = datetime.date.today()
    yesterday = to_day - datetime.timedelta(1) #Giả sử bạn cần đọc file log ngày hôm qua
    file_name = "u_ex%s%s%s.log" % (yesterday.year, yesterday.month, yesterday.day)
    return file_name

file_name = get_file_name()

with open(file_name, 'r') as f:
read_data = f.read()
 # Do Something
