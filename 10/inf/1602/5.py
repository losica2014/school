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
            p += (printNum((n//10**i)%10**i, woe=True) + 'сти ')
        if(i == 1):
            ta = n//10
            t = ta%10
            t0 = (n//10)%10
            if(n % 100 > 10) and (n % 100 < 20):
                p += printNum(t0, woe=True)
                p += 'надцать '
                break
            else:
                if(t == 1):
                    p += 'десять'
                elif(t >= 2 & t < 4):
                    p += printNum(t, woe=True)
                    p += 'дцать '
                elif(t == 4):
                    p += 'сорок '
                elif(t >= 5 & t < 9):
                    p += printNum(t, woe=False)
                    p += 'десят '
                elif(t == 9):
                    p += 'девяносто '
        if(i == 0):
            p += printNum(n%10, woe=False)
    print(p)
    
printWords(int(input()))
