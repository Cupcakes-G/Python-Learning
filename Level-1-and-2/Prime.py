##finds first x prime nums
def primes(x):


    primeList = []
    count = 0
    num = 2

    while ( count <= x):
        p = is_prime(num)
        if (p ):                  #is p is true
            primeList.append(num)
            count = count + 1

        num = num +1

    return primeList




# return True if num is Prime else False
def is_prime(num):
    lis = range(2,num/2)
    for x in lis:
        if (num % x == 0):

            return False

    return True


# main
print primes(1000)