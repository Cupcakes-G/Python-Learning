

file = open("hello.txt", "w")

file.write("happy llama\n")

file.write("sad llama\n")
s = 9
h = "hi"
file.write(str(s) + "\n")           #use + to addd strings
file.write(h)

file.close()

line  = open('hello.txt', 'r')

for x in line:
    #for y in x:
        #print y
    print x



