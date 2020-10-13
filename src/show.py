import calendar
import time

cal=calendar.month(2020,12)
print("以下输出为2020年12月日历：")
print(cal)

"""time=time.clock()"""

print(time)

cal_name=dir(calendar)
print("CALENDAR_NAME:",cal_name)
time_name=dir(time)
print("TIME_NAME:",time_name)