#finds the divisors of a given number (13 is a divisor of 26)#4
def divisors(num):
    new = []
    ran = range(1,num + 1)
    for x in ran:
        if (num%x == 0):
            new.append(x)
    return new

num = int(raw_input("Choose A Number To Find The Divisors Of:"))
print (divisors(num))
