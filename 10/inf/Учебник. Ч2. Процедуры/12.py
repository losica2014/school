# 1     I
# 5     V
# 10    X
# 50    L
# 100   C
# 500   D
# 1000  M

def numToRomanian(nn):
    n = str(nn)
    r = ""

    for i in range(0, len(n)):
        c = len(n)-i-1
        d = int(n[i])
        if(c == 0):
            if(d == 9):
                r+='IX'
            if(d>=5 and d<9):
                r+='V' + 'I'*(d-5)
            if(d == 4):
                r+= 'IV'
            if(d < 4):
                r+= 'I'*(d)
        if(c == 1):
            if(d == 9):
                r+='XC'
            if(d>=5 and d<9):
                r+='L' + 'X'*(d-5)
            if(d == 4):
                r+= 'XL'
            if(d < 4):
                r+= 'X'*(d)
        if(c == 2):
            if(d == 9):
                r+='CM'
            if(d>=5 and d<9):
                r+='D' + 'C'*(d-5)
            if(d == 4):
                r+= 'CD'
            if(d < 4):
                r+= 'C'*(d)
        if(c == 3):
            r+= 'M'*(d)
        if(c > 3):
            r+= 'M'*((10**(c-3))*d)

    print(r)

numToRomanian(int(input()))