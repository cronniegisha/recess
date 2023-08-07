print("after lunch")
print('after prep')

y=("after lunch")
print(y)

#multiline strings
intro=""" I work during day
so, its not possible for me to create time 
for you during the week.
Kindly reschedule.
"""
print(intro)
print(intro[103])

#strings in arrays
day="morning","afternoon","evening","night"
print(day[2])

#check presence of a string
COCIS="there are only boys at cocis."
print("girls" in COCIS)
print("boys" in COCIS)
#using the if to check
if "girls" in COCIS:
    print("yes please")
else:
    print("sorry, no girls allowed.")

#exercise 1
print(len(day))
print(len(intro))

#exercise 2
#using the for loop in a string
#we loop through characters
for y in "banana":
    print(y)

day="morning","afternoon","evening","night"
for x in day:
    print(x)


#exercise 3
#slicing strings
#returns a range of characters.
OS="Welcome to your Windows."
print(OS[:3])
print(OS[3:])
print(OS[1:3])

#modifying Strings
print(OS.upper())#returns the string in uppercase
print(OS.lower())#returns the string in lowercase
#removing whitespaces
OS="    Welcome to your Windows.   "
print(OS.strip())
#replacing String
print(OS.replace("Windows", "Apple OS"))