A = 1
while True:
    e = False
    for x in range(1, 1000):
        if(((x % 84 != 0) or (x % 90 != 0)) <= x % A != 0) == False:
            e = True
            break;
    if not e:
        print(A)
        break
    A += 1
