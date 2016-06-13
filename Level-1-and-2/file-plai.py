

from palindrome import panagram


#main
name = raw_input("What is the name of your file-- ") # raw_input() for Python 2.7 ,  input() for Python 3.0
filename = "myfiles/" + name

b = open( filename, 'r')
for x in b:   #x is each line
    y = x.strip()
    if panagram(y):
        print y
