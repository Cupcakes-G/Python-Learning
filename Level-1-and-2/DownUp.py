##prints nums from zero to a given n, then back to zero
######FUNCTION
def DownUp(n):
    k = n
    lis = []
    go = True
    down = True
    while (go):
        lis.append(k)
        if (k > 0 and down):
            k = k - 1
        elif (k == 0):
            #lis.append(k)
            k = k + 1
            down = False
        elif (len(lis) == 2 * n + 1):
            go = False
        else:
            k = k + 1

    return lis

print (DownUp(4))