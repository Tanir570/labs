def squer(n):
    for i in range(n=1):
        yield i**2
    for i in squer(10):
        print(i)