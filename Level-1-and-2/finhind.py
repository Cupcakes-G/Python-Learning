

def big_num(lis):
    bind = 0
    ind = 0
    for x in lis:
        if (x > lis[bind]):
            bind = ind
        ind = ind + 1
    return bind






#Main program
a = [78,4,5,3,5,7,4,5,42,867,3,45,-439443392, 337, 9]
pos = big_num(a)
print pos , a[pos]

