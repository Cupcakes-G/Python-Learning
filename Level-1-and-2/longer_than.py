##returns words that are longer than a given number

def filter(lis, n):
    newlis = []
    for x in lis:
        a  = len(x)
        if (a > n):
            newlis.append(x)
    return newlis

# main
c = ["hi", "my", "name", "is","githika"]
g = 3
a = filter(c,g)
print a