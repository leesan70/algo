from itertools import permutations


def isValidHour(hour):
    return 0 <= hour < 24


def isValidMinute(minute):
    return 0 <= minute < 60


def formatStr(time):
    return "0" + str(time) if time < 10 else str(time)


def largestTimeFromDigits(arr):
    largestHour = 0
    largestMinute = 0
    validTimeFound = False
    for p in permutations(arr, 4):
        hour = 10 * p[0] + p[1]
        minute = 10 * p[2] + p[3]
        if isValidHour(hour) and isValidMinute(minute):
            validTimeFound = True
            if hour > largestHour:
                largestHour = hour
                largestMinute = minute
            elif hour >= largestHour:
                largestMinute = minute if minute > largestMinute else largestMinute
    return formatStr(largestHour) + ":" + formatStr(largestMinute) if validTimeFound else ""
