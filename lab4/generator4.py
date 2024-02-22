def squer(a, b):
    for i in range(a, b+1):
        yield(i**2)
a=3
b=37
for i in squer(a, b):
    print(i)