from datetime import datetime, date, timedelta

#datetime.now() : fulldate + time
print(datetime.now())

#date.today():
print(date.today())

#now.strftime(format_string) format to a string
timenow = datetime.now().strftime("%Y-%m-%d %H:%M")
print(timenow)
timenow = datetime.now().strftime("%d-%m-%Y %H:%M")
print(type(timenow))

#datetime.strptime(text, format_string):
dt = datetime.strptime("2023-01-14", "%Y-%m-%d")
print(type(dt))

#timedelta : use to add or subtract days, hours...
tomorrow = date.today() + timedelta(days=35)
print(tomorrow)

one_hour_ago = datetime.now() - timedelta(hours=3)
print(one_hour_ago)