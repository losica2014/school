A = 1
while True:
    e = False
    for x in range(1, 1000):
        #if(A == 21) or (A == 40):
        #    e = True
        #    break;
        if((21 % A == 0) and (((x % 40 == 0) and (x % 30 == 0)) <= (x % A == 0))) == False:
            e = True
            break;
    if not e:
        Amax = A
    A += 1
    if(A > 100000):
        break
print(Amax)
