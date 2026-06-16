from datetime import datetime
import calendar

def check_month_difference(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")

    if d1 > d2:
        d1, d2 = d2, d1

    month = d1.month + 1
    year = d1.year

    if month > 12:
        month = 1
        year += 1

    days_in_month = calendar.monthrange(year, month)[1]

    if d1.day <= days_in_month:
        next_month_same_day = d1.replace(year=year, month=month)
    else:
        next_month_same_day = d1.replace(year=year, month=month,
                                         day=days_in_month)

    if d2 == next_month_same_day:
        return "Exactly 1 month apart"
    elif d2 < next_month_same_day:
        return "Less than 1 month apart"
    else:
        return "More than 1 month apart"

# Examples
print(check_month_difference("06-06-2011", "06-07-2011"))
print(check_month_difference("01-03-2011", "25-03-2011"))