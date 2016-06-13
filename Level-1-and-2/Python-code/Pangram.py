#finds if a string is a panagram(sentence that has all the letters of the alphabet in it)
def panagram(str):
    dict = {}
    for x in str:
        if x in dict.keys():
            dict[x] = 1 + dict[x]
        else:
            dict[x] = 1
    return dict

h = "githika"
print (panagram(h))
