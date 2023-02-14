#This is a program to test if a given year is leap or not.

def is_leap(year):
    leap = False

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            return False
        return True
    return False

year = int(input())
print(is_leap(year))
