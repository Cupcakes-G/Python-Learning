
class person:
    name = "name"
    age = 12
    grade = "C"

filep = open('names.txt', 'r')

students = []
for line in filep:
    record = line.split(" ")

    p = person()
    p.name = record[0]

    p.age =record[1]

    p.grade = record[2]

    students.append(p)

for x in students:
    print x.name , x.age , x.grade











