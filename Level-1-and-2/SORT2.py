##############

def sort_list(lst):

    new_list = []
    copy_list = list(lst)

    for x in lst:
        big_ind = big_index(copy_list) #finds the index of biggest number in copy list calling function below
        b = copy_list[big_ind] # finds biggest number in copy list
        new_list.append(b) # adds b (biggest number) to the new list
        del copy_list[big_ind] # deletes the biggest number from copy list

    return new_list

##############
def big_index(lis):

    big_index = 0
    index  = 0
    for x in lis:
        if (x < lis[big_index]):
            big_index = index

        index = index + 1

    return big_index

#Main program
a = [15,12,5,55,6,9,47,8,35,3,22,26,46,54,17,42,43,42,15,5]
final_list = sort_list(a)
print final_list
