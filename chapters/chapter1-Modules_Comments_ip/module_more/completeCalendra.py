import calendar

# Example: Print the full year 2015 starting with Sunday
c = calendar.TextCalendar(firstweekday=6)  # 6 = Sunday
print(c.formatyear(2026))
