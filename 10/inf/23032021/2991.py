A = 1
while True:
    e = False
    for x in range(1, 1000):
        #if(A == 21) or (A == 40):
        #    e = True
        #    break;
        if((((x % A == 0) and (x % 45 == 0)) <= (x % 162 == 0)) and (A > 200)) == False:
            e = True
            break;
    if not e:
        print(A)
        break
    A += 1
