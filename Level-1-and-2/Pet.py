## using classes for the first time
class person:
    eye_color = "blue"
    name = "girl"
    age = 13
    def eat(self):
        print "nom nom nom"

p = person()
p.name = "Githika"
p.eye_color = "brown"

lis = []
lis.append(p)

p = person()
p.name = "Manju"
p.eye_color = "purple"
p.age = 12

lis.append(p)

for a in lis:
    if (a.age > 12):
        print a.name , "IS ", a.age , " younger"
    else:
        print a.name , "IS ", a.age , " older"


#gitu.eat()  #wwwoooaaaaahhhh you dont even need to type print!! cause its says print above
#print "gitu's eyes are %s " %gitu.eye_color  #wwoooaahh %s is like a * in writing