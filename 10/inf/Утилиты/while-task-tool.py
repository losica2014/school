answ = []

for x in range(1, 1000):
    xo = x
    
    # Start of given program
    
    a = 0; b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 8)
        x = x // 8
        
    # End of given program
    
    # Check for conditions
    if(a == 3) & (b == 24):
        answ.append(xo)

r = answ[0]
print(answ)
for i in answ:
    if(i > r):
        r = i
print(r)
