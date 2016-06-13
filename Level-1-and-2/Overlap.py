#returns overlaping elements from two lists
#5
def overlap(lis,lst):
    overlap = []
    for x in lis:
        for y in lst:
            if (x == y):
                if (not(x in overlap)):
                    overlap.append(x)
    return overlap


o = [1,2,3,4,5, "hi", "hello"]
p = [4,5,6,7,8, "hi", "sup"]
print (overlap(o,p))

#14
"""
def list(lis):
  new = []
  for x in lis:
    if x not in new:
      new.append(x)
  return new

f = [2,2,3]
print (list(f))
"""






















