##finds primes between two numbers
"""
def prime(x,y):
    primes = []
    c = range(x,y)
    for x in c:
        p = is_prime(x)
        if (p):#sees is p is true
            primes.append(x)
    return primes
"""


# return True if num is Prime else False
def is_prime(num):
    lis = range(2,num/2)
    for x in lis:
        if (num % x == 0):

            return False

    return True

# main
print prime(5,149)