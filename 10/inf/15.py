a = int(input())
for n in range(1, 1000):
    r = n
    for i in range(n-1, 0, -1):
        r = r * i
    
    if(r == a):
        print(n)
