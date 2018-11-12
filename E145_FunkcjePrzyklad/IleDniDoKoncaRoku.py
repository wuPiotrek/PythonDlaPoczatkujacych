#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

def DaysTillEndYear():

    from datetime import date, timedelta

    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)

    return

DaysTillEndYear()

#################################################
