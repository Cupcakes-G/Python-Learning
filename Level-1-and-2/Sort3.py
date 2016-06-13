#this was the old 1
#finds  bigest/smallest  #'s  0F   A     LIST
#function

def sort_list(lis):
    new = []
    copy = list(lis)
    for x in lis:
        b = big_index(copy)
        num = copy(b)
        new.append(num)
        del copy[b]

    return new

##############
def big_index(lis):

    big_index = 0
    index  = 0
    for x in lis:
        if (x > lis[big_index]):
            big_index = index

        index = index + 1

    return big_index

#Main program
a = [7,4,5,3,5,7,4,5,42,7,3,45,-439443392, 33827, 9]
final_list = sort_list(a)
print final_list

