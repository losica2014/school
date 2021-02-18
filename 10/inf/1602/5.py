def printNum(n, woe=False):
    if(n == 1):
        return 'Один'
    if(n == 2):
        if(woe):
            return 'Две'
        else:
            return 'Два'
    if(n == 3):
        return 'Три'
    if(n == 4):
        if(woe):
            return 'Четыр'
        else:
            return 'Четыре'
    if(n == 5):
        if(woe):
            return 'Пят'
        else:
            return 'Пять'
    if(n == 6):
        if(woe):
            return 'Шест'
        else:
            return 'Шесть'
    if(n == 7):
        if(woe):
            return 'Сем'
        else:
            return 'Семь'
    if(n == 8):
        if(woe):
            return 'Восем'
        else:
            return 'Восемь'
    if(n == 9):
        if(woe):
            return 'Девят'
        else:
            return 'Девять'
    if(n == 0):
        if(woe):
            return ''
        else:
            return 'Ноль'
    
def printWords(n):
    p = ""
    for i in range(len(str(n))-1, -1, -1):
        if(i == 2):
            ta = n//100
            t = ta%10
            if(t == 1):
                p += 'Сто '
            if(t == 2):
                p += 'Двести '
            if(t >= 3) and (t < 5):
                p += (printNum((n//10**i)%10**i, woe=True) + 'ста ')
            if(t >= 5) and (t <= 9):
                p += (printNum((n//10**i)%10**i, woe=False) + 'сот ')
        if(i == 1):
            ta = n//10
            t = ta%10
            t0 = (n//10)%10
            tn = n % 100
            print(n % 100)
            if(tn > 10) and (tn < 20):
                p += printNum(t0, woe=True)
                p += 'надцать '
                break
            elif(tn == 10):
                p += 'Десять'
            elif(tn >= 20) and (tn < 40):
                p += printNum(t, woe=True)
                p += 'дцать '
            elif(tn == 4):
                p += 'сорок '
            elif(tn >= 50) and (tn < 90):
                p += printNum(t, woe=False)
                p += 'десят '
            elif(tn >= 90):
                p += 'Девяносто '
        if(i == 0):
            p += printNum(n%10, woe=False)
    print(p)
    
printWords(int(input()))
