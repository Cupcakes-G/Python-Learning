


f = open("myfiles.h2",'w')  ##myflies is the folder name, and h2 is the file name, if their is no folder no . needed id file name is variable no ""

f.write(" first line\n") #  \n = new line

f.write(" line 2 in file\n")
f.write(" line 3 in file\n")
f.close()



# now read the file  'r'
# r=read   w=write erases whatever is in the file and puts the new stuff    a=append at end
b = open("myfiles/h",'r')
for x in b:   #x is each line
    print x

b.close()


