import datetime
from datetime import timedelta
count = int(raw_input())
expectedDate = datetime.datetime.strptime(raw_input(), '%d-%m-%Y')

expectedDate = expectedDate + timedelta(days=count)
print expectedDate.strftime('%d-%m-%Y')
