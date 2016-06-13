#takes a list of words and returns numbers corresponding to the words' lengths
def idk(lst):
    numbers = []
    for  x in lst:
        f = len(x)
        numbers.append(f)
    return numbers

i = ["hi", "westside", "just", "later", "opposite"]
print(idk(i))
