import math
n = int(input())
l = float(input())
s1 = (n*l**2)/(4*math.tan(math.pi/n))
s = round(s1)
print(s)