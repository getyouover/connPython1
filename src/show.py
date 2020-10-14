import calendar
import time

from pip._vendor.distlib.compat import raw_input

from src import test

cal = calendar.month(2020, 12)
print("以下输出为2020年12月日历：")
print(cal)

# time = time.clock()

# print(time)

test.show()
cal_name = dir(calendar)
print("CALENDAR_NAME:", cal_name)
time_name = dir(time)
print("TIME_NAME:", time_name)

str_1 = raw_input("请输入:\n")

print(str_1)

str_2 = input("请输入：\n")

print(str_2)

file_fo = open("test.txt", "a")
file_fo.write("123456789123456789\n")
file_fo.flush()
file_fo.close()
