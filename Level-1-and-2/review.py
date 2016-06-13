
#finds  bigest/smallest  #'s  0F   A     LIST
#function
def big_num(lis):
    c = lis[0]
    b = lis[0]
    for x in lis:
        if (x > b):
            b = x

        if (x < c):
            c = x

    return c, b

#Main program
a = [7,4,5,3,5,7,4,5,42,7,3,45,-439443392, 33827]
f = big_num(a)
print f

