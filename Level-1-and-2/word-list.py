#returns a list of nums length of the words in a list
def nums(lis):
    new_lis= []
    for x in lis:
        a = lng(x)
        new_lis.append(a)
    return new_lis

def lng(x):
    a = 0
    for g in x:
        a = a + 1
    return  a



def longstr(lis2):

    lis = nums(lis2)
    bigind = 0
    ind  = 0

    for x in lis:

        if (x > lis[bigind]):
            bigind = ind

        ind = ind + 1

    return lis2[bigind]



#main
a = ["hi", "shack", "mansion", "appartment", "house"]
v = nums(a)
print v
print longstr(a)