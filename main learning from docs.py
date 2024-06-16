import datetime

dt = datetime.datetime(2024, 1, 11)

formatted_date = dt.strftime("%a")
print("Abbreviated Weekday Name:", formatted_date)


formatted_date = dt.strftime("%A")
print("Full Weekday Name:", formatted_date)

formatted_date = dt.strftime("%w")
print("Full Weekday Name:", formatted_date)

formatted_month_abbrev = dt.strftime("%b")
print("Abbreviated Month Name:", formatted_month_abbrev)

formatted_month_full = dt.strftime("%B")
print("Full Month Name:", formatted_month_full)




for i in range(1,13):
    dt = datetime.datetime(2024, i, 11)
    formatted_month_full = dt.strftime("%B")
    formatted_month_abbrev = dt.strftime("%b")

    print("Abbreviated Month Name:", formatted_month_abbrev)
    print("Full Month Name:", formatted_month_full)