from datetime import datetime
from datetime import timedelta

days = {'Monday': 1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday': 6, 'Sunday': 7, 'monday': 1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday': 6, 'sunday': 7}

day = raw_input()
n=int(raw_input())
start_date=raw_input()

date_obj=datetime.strptime(start_date,"%d-%m-%Y")

x = int(days[day])

for i in range(1,n):
    x = x + 1
    if x == 6:
        date_obj=date_obj+timedelta(days=3)
        print (date_obj.strftime("%d-%m-%Y"))
        x = 1
    elif x == 7:
        date_obj=date_obj+timedelta(days=1)
        print (date_obj.strftime("%d-%m-%Y"))
    else:
        date_obj=date_obj+timedelta(days=1)
        print (date_obj.strftime("%d-%m-%Y"))