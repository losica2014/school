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
        return 'Ноль'
    
def printWords(n):
    p = ""
    for i in range(len(str(n))-1, 0, -1):
        if(i == 1):
            p += printNum(n%10**i, woe=True) + 'надцать'
    print(p)
printWords(int(input()))

