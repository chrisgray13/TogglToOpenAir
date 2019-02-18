from datetime import datetime

def roundDuration(duration):
    overage = duration % 0.25000
    if overage >= 0.125000:
        return round(duration + (0.25000 - overage), 2)
    else:
        return round(duration - overage, 2)

def getDay(date):
    return datetime.strptime(date, "%Y-%m-%d").day

def getDayOfTheWeek(date, sundayPosition=1):
    if sundayPosition < 1 or sundayPosition > 7:
        raise ValueError("sundayPosition must be in the range of 1 to 7 => {0}".format(sundayPosition))

    weekday = datetime.strptime(date, "%Y-%m-%d").isoweekday() # Sunday = 7
    weekday = weekday + sundayPosition
    if weekday > 7:
        weekday = weekday - 7
    
    return weekday
