# import sys

# print(sys.path)

from datetime import datetime, timedelta, date

"""
dt_now = datetime.now()
print(dt_now)
dt2 = datetime(2015, 5, 16, 8, 3, 44)
delta = dt_now - dt2
print(delta)
from datetime import date, timedelta

dt = date(2000, 1, 1)
print(dt)
delta = timedelta(days=1)
print(delta)
dt_now = datetime.now()
print(dt_now.strftime('%d.%m.%Y %H:%m'))
print(dt_now.strftime('%Y-%m-%d'))

import locale

loc = locale.getlocale()

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
print(dt_now.strftime('%A %d %B %Y'))

date_string = '12/23/2021'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
"""
delta = [1, 0, 30]
for i in delta:
	print(datetime.now() - timedelta(days=i))

date_str = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)

