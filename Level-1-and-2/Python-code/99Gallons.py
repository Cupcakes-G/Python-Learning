#prints all the verses to the sond "99 gallons of milk on the wall"
def milk():
    b = 100
    s = " "
    while (b > 1):
        gm = " gallons of milk"
        gmw = gm + " on the wall "
        b = b - 1
        td = " take one down, pass it around, "
        gm2 = " gallon of milk "
        gmw2 = gm2 + " on the wall, "
        nm = "no more gallons of milk on the wall."
        c = ","
        sc = ";"
        if (b == 1):
            s =  str(b) + gmw2 + str(b) + gm2 + c +td + nm
        else:
            s =  str(b) + gmw + str(b) + gm + c + td + str(b - 1) + gmw + sc
        print (s)


milk()
