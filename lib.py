def func (mas):
    N = len(mas)
    n = len(mas[0])
    k = 0
    for i in range (n):
        t = True
        for j in range (1, N):
            if (mas[0][i] in mas[j]) != True:
                t = False
                break
        if t == True:
            k = k + 1
    return k