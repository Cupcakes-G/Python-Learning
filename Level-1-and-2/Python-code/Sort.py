#sorts numbers in a list in least to greatest order
def small(lst):
    y = lst[0]
    for x in lst:
        if x < y:
            y = x
    return y

def sort(y):
    lst = y
    sorted = []
    k = lst[0]
    while (len(lst) > 0):
        u = small(lst)
        sorted.append(u)
        lst.remove(u)
    return sorted

lis = [3,57,2,6,2,9,10,1]
o = sort(lis)
print (o)









