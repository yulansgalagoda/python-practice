# epoch = a date and time from which a computer measures system time. Machine thinks it's when time started

import time

# ctime convert a time expressed in seconds since epoch to a readable string
# epoch is when the computer thinks time began (reference point)
print(time.ctime(0))

# seconds passed from epoch until now
print(time.time())

# current time in a readable format
print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H %M %S", time_object)    # strftime = string format time
print(local_time)

time_object = time.gmtime()
local_time = time.strftime("%B %d %Y %H %M %S", time_object)
print(local_time)

time_string = "20 April, 2022"
time_object = time.strptime(time_string, "%d %B, %Y")     # string representation
print(time_object)

# (year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# (year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
