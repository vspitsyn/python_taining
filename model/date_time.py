import datetime
import random

def isLeapYear(year):
    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        return True
    else:
        return False


def randomDate(date1, date2):
    delta = date2 - date1
    return date1 + datetime.timedelta(random.randrange(0,delta.days,1))

# months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August',
#           9:'September', 10:'October', 11:'November', 12:'December'}

def month_name(n):
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return months[n]

# print(month_name(6))
#print(randomDate(datetime.date(2000,1,1), datetime.date(2017,1,1)))
# print(randomDate(datetime.date(2000,1,1), datetime.date(2017,1,1)).year)
# print(month_name(randomDate(datetime.date(2000,1,1), datetime.date(2017,1,1)).month))
# print(randomDate(datetime.date(2000,1,1), datetime.date(2017,1,1)).day)
