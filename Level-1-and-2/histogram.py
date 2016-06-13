### makes a histogram for the numbers in a list

def hist(n):
    for x in n:
        cnt = 0
        stars = ""
        while(cnt < x):
            stars = stars + "* "
            cnt = cnt + 1
        print stars

# main
a = [6,7,4,7,9,0,2,2]     #doesn't work 4 negative #'s
b = hist(a)
