def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

print(f"Is 1900 a leap year? {is_leap_year(1900)}")

