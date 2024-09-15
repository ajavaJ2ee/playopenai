from datetime import datetime, timezone, timedelta

#Naive datetime object
print(datetime.now())

#Aware datetime object
print(datetime.now(timezone.utc))

today=datetime.now(timezone.utc)
print(today)
tomorrow= today+timedelta(days=1.5)
print(tomorrow)

#String format time
print(today.strftime('%d %m %Y %H:%M:%S'))

user_date=input('Enter date in YYYY-mm-dd format: ')
#string parse time
user_date_parsed=datetime.strptime(user_date,'%Y-%m-%d')

print(f'parsed date:{user_date_parsed}')




#print(datetime.now(timezone.utcoffset(tomorrow)))


