import sys
location = sys.path
# print(location)
for i in location:
    print(i)

# geeting the number of leapdeys between 2000 to 2050
import calendar
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

# determining weather a year is a leap year
isLeapYear = calendar.isleap(2036)
print(isLeapYear)

