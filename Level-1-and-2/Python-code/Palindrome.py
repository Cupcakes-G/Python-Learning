# function returns a Reverse of INPUT string
def reversestr(str):
    newstr = ""
    x = len(str)
    while (x > 0):
        x = x - 1
        newstr = newstr + str[x]

    return newstr

# returns True if INPUT string and Reverse of it are SAME
def palindrome(str):
    rev = reversestr(str)
    return ( str == rev)

# removes puntuation characters such as "." ";"  from INPUT and returns CLEANED string
def cleanstr(str):
    clean = ""
    x = len(str)
    while (x > 0):
        x = x - 1
        ispunc = (( str[x] == ".") or (str[x] == ";"))
        if (not (ispunc)):
            clean = clean + str[x]

    return clean


#main program
#program finds if a string is a palindrome (same backwards and front) despite punctuation
str = input("enter a string:")
clean = cleanstr(str)
#print ( clean)
if palindrome(clean):
    print ( str + " :is a Palindrome" )
else:
    print ( str + " :is NOT a Palindrome" )
