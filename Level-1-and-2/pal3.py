#####FFFUUUNNNCCCCTTTIIIIOOOONNNN!!!!!!!

def pali(str):
    count = 0
    n = len(str)
    while (n >= count):
        n = n - 1
        if ( str[n] == str[count]):
            count = count + 1
        else:
            return False

        print n

    return True

####    MMMMAAAAAIIIIINNNN   PPPRRROOGGGRRAAAMMMMMM!!!!!!!!
#m'kay i get it now
print pali("lkdadklkk")
print 33



