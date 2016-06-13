#function..
def DownUp(n):
    k = 2 * n + 1
    h = n
    while (k > 0):
        k = k - 1

        if (h < 0) :
            print h * -1
        else:
           print h

        h = h - 1

#main
print DownUp(9)