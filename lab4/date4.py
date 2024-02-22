import datetime 
d1 = datetime.datetime.today()
d2= datetime.datetime.today()
diff =d1 - d2
m = diff.microseconds
print(m)