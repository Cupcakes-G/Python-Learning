#returns palindrome(words that read the same backwards and front) despite punctiation, capitilization, and spacing
#6
def panagram(str):
    count = len(str)
    length = count
    nwlis = ""
    originalList = ""

    while (count > 0):

        c = str[count - 1]
        if (c == ",") or (c == " ") or (c == ".") or (c == "'") or (c == ";")or (c == "?"):
            pass
        else:
            nwlis = nwlis + c

        c = str[length - count]
        if (c == ",") or (c == " ") or (c == ".") or (c == "'") or (c == ";") or (c == "?"):
            pass
        else:
           originalList = originalList + c

        count = count - 1


    if nwlis.lower() == originalList.lower():
        return True
    else:
        return False

#main
str2 = "MoM"
#print panagram(str2)

#Yay it works http://tutorindia.net/Tutor_Profiles-NDE1NTE-highly_recommended_maths_chemistry_physics_teacher

#solution on chilli website
#a)
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

#b)
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
		return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')