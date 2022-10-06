def strangeAlg(a):
    b = a[0]
    c = 0
    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if(a[i][j] in b):
                c+=1
        b.append(a[i])
    return c