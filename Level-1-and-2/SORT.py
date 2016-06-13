
#this was the old 1
#finds  bigest/smallest  #'s  0F   A     LIST
#function
def big_num(lis):

    big_index = 0
    index  = 0
    for x in lis:
        if (x > lis[big_index]):
            big_index = index

        index = index + 1


    return big_index

#Main program
a = [7,4,5,3,5,7,4,5,42,7,3,45,-439443392, 33827, 9]
pos = big_num(a)
print pos , a[pos]


def order_nums(lis):
    new =[]
    a = 0
    copy = lis
    for x in copy:
        if x > lis[a]:
            a = a + 1
            del copy[x]
            new.append(x)


#Main program
d = [7,4,5,3,5,7,4,5,42,7,3,45,-439443392, 33827, 9]
c = order_nums(d)
print c