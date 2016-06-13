#this project thing returns nums in a list that are greater than the average

#function
def abv_avg(lis):
    length = 0
    sum = 0
    new=[]
    for x in lis:
        sum = sum + x
        length = length + 1
    avg = sum/length
    for x in lis:
        if x > avg:
            new.append(x)

    return new


#main
h = [1,2,3,4,5,6,7,8,9]
print abv_avg(h)


