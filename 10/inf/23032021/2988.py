A = 1
while True:
    e = False
    for x in range(1, 1000):
        #if(A == 21) or (A == 40):
        #    e = True
        #    break;
        if((((x % A == 0) <= (x % 54 == 0)) or (x % 130 == 0)) and (A > 60)) == False:
            e = True
            break;
    if not e:
        print(A)
        break
    A += 1
