import calendar

day,year,month = 10,2025,11
day_index = calendar.weekday(year,month,day)
days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(days[day_index])
