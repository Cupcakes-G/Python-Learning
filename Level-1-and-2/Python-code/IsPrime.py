# finds if a number is prime
def IsPrime(n):
    y = range(2,n + 1)
    for x in y:
        h = int(n/x)
        if (h * x == n):
            return False
        else :
            return True

g = 4
print (IsPrime(g))


# finds first five prime numbers between a given 2 numbers
def FirstFive(n,m):
    lis = range (n, m +1)
    new_list = []
    b = 0
    for x in lis:
        if (b == 5):
            break
        if IsPrime(x):
            b = b +1
            new_list.append(x)
    return new_list

print (FirstFive(1,9))
