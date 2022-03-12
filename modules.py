# import random
# print(random.randint(1,10))
# print(random.randint(1,10))
# print(random.randint(1,10))
# print(random.randint(1,10))

import datetime
# Datetime is written twice as datetime module contains datetime class which contains now() method
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now + datetime.timedelta(days = 10)) #This will give the date of 10 days after the current date