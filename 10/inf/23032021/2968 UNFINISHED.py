A = 1
while True:
    e = False
    for x in range(1, 1000):
        #if(A == 21) or (A == 40):
        #    e = True
        #    break;
        if((((x % 36 == 0) and (x % 42 == 0) and (x % 126 == 0)) and (A > 1000)) == False:
            e = True
            break;
    if not e:
        print(A)
        break
    A += 1
