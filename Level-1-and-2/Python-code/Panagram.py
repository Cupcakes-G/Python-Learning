#finds if pangram, or string with every letter of the alphabet in it
def panagram(str):
    num = 65
    d = dict()
    while (num < 90):
        c = chr(num)
        d[c] = 0
        num = num + 1

    for x in str:
        x = x.capitalize()
        if x in d:
            d[x] = d[x] + 1

    for x in d.values():
        if x == 0:
            return False

    return True


ret = panagram("qwertyuiopasdfghjklzxcvbnm   ....///;';")
print (ret)
