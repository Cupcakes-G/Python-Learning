def char_freq(str):
    d = dict()
    for x in str:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    return d

char = "abcdababababaaaaaaa"
print(char_freq(char))