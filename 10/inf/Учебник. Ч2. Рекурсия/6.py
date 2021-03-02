def MGD_recursive(n1, n2):
    if(n1 == 0) or (n2 == 0):
        print(n1+n2)
        return
    if(n1 > n2):
        MGD_recursive(n1-n2, n2)
    else:
        MGD_recursive(n1, n2-n1)

def MGD_nonrecursive(n1, n2):
    while(n1 != 0) and (n2 != 0):
        if(n1 > n2):
            n1 -= n2
        else:
            n2 -= n1
    print(n1+n2)

n1 = int(input('N1: '))
n2 = int(input('N2: '))

MGD_recursive(n1, n2)
MGD_nonrecursive(n1, n2)
