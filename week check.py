from parking_pass import pass_generator
import datetime
from datetime import date
import calendar

day = input("Enter the weekday")

@pass_generator
def Weekday_check(value):
    my_date = date.today()
    # weekday = calendar.day_name[my_date.weekday()]
    if day == "Monday" or day == "Wednesday" or day == "Friday" :
         pass
    else: 
        print("passes are available only on Monday, wednesday and Friday")


Weekday_check(day)
