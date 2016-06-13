#returns numbers in a list smaller than p by putting them in another list (#3)

def small(lis, p):
    new = []
    for x in lis:
        if (x < p):
            new.append(x)
    return new





def smaller(lis,p):
    print([ i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < p])

##one line codes
#[i*i for i in [1, 2, 13, 21, 34, 55, 89] if i < 30 ]
#[1, 4, 169, 441]


#main
list = [1,2,3,4,5,6,7,8,0,-32423534,9,10,20,303,405060,7,80909,9,0]
num = int(raw_input("Choose a number: "))

print (smaller(list, num))

#7
#finds even elements in a list
def even (lis):

    return [ x for x in lis if (x%2 == 0)]

a = [1, 2,3,4,5,6,7,8,9,10]
print (even(a))

#make this one line