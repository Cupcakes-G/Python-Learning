#####FFFUUUNNNCCCCTTTIIIIOOOONNNN!!!!!!!

def showpairs(n):
    count = 0
    biglis = []
    while (n > 0):
        n = n - 1

        lis2 = []
        lis2.append( n)
        lis2.append(count)

        biglis.append(lis2)
        #print n, count
        count = count + 1

    return biglis

####    MMMMAAAAAIIIIINNNN   PPPRRROOGGGRRAAAMMMMMM!!!!!!!!
#m'kay i get it now
p = showpairs(15)
for x in p:
    print x[0], x[1]


