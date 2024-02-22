import datetime
d1 = datetime.datetime.today()
d1=d1- datetime.timedelta(days=1)
d2 = datetime.datetime.today()
d2 = d2 + datetime.timedelta (days =1)
print("Yesterday:", d1)
print ("Today:", datetime.datetime.today())
print("Tommorow:", d2)