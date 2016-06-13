#i don't even know
def Sweeden(sen):
    d={'merry':'god','christmas':'jul ','and':'och','happy':'gott','new':'nytt','year':'år'}
    z = sen.split(" ")
    s = ""
    for x in z:
        i = d[x]
        s = s + ' ' + i
    return s
#main
p = "merry christmas and happy new year"
print (Sweeden(p))