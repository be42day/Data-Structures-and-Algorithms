month_30 = [4,6,9,11]
month_31 = [1,3,5,7,8,10,12]

def is_leap(year):
    """Checks if a year is leap or not"""
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def nextDay(year, month, day):
    """Returns the next day date"""
    if month in month_30:
        if day < 30:
            return year, month, day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1
    
    elif month in month_31:
        if day < 31:
            return year, month, day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1
            
    else:
        if is_leap(year):
            if day < 29:
                return year, month, day + 1
            else:
                if month == 12:
                    return year + 1, 1, 1
                else:
                    return year, month + 1, 1
        else:
            if day < 28:
                return year, month, day + 1
            else:
                if month == 12:
                    return year + 1, 1, 1
                else:
                    return year, month + 1, 1
        
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
       
    # Throw an AssertionError if the input is not valid
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days