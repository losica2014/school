c = 0
def F(n):
    global c
    # print('*')
    c += 1
    if(n >= 1):
        # print('*')
        c += 1
        F(n-1)
        F(n-2)

F(28)
print(c)
