'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def e19():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    day = 1
    count = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            if year > 1900 and day == 6:
                count += 1
            day += months[month]
            if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day += 1
            day %= 7
    return count    
import time
start = time.time()
print(e19())
print("Time elapsed:", time.time() - start, "seconds")
#171