###checks if a string is a plaindrome using the up down method
def palindrome (str):
    pali = str
    b = 0
    e = (len(pali)) + 1
    #g = (len(pali)) / 2
    while (b <= g):
        if (pali[b] == pali[e]):
            b = b + 1
            e = e - 1

        else:
            return False
    return True

#main
h = "hellodadolleh"
print (palindrome(h))





