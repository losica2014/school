for i in range(10,1000):
    if((i**3 % 100 == i and i < 100) or (i**3 % 1000 == i and i >= 100)):
        print(i, i**3)
