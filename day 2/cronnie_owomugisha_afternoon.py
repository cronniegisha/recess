#they used to store key:value pairs
mydict={
"phone":"samsung",
"model":"S10",
"manufacturer":"android",
"colors": ["blue","red","green"]
}
print(mydict)

print(len(mydict))

print(type(mydict))

#accessing Dictionary items
z=mydict["colors"]
print(z)

w=mydict.keys()
print(w)

#exercise 1
y=mydict.values()
print(y)


#dict()constructor
phoneshop=dict(
phone="samsung",
model="S10",
manufacturer="android")

print(phoneshop)

#exercise 2
if "phone" in phoneshop:
    print("we remember the phone")
else :
    print("sorry, we dont know whatyou are asking for")

#exercise 3
#changing the values
phoneshop["phone"]= "nokia"
print(phoneshop)

#using the update
phoneshop.update({"manufacturer": "google"})
print(phoneshop)

#exercise 4
#adding items
shop=dict(
car="BMW",
model=2003,
manufacturer="mercedes")
shop["color"]={"silver","black"}
print(shop)

#removing items
shop.pop("model")
print(shop)

#del("manufacturer")

#exercise 5
#looping through
for x in shop:
    print(x)

#displaying values
for x in shop:
    print(shop[x])   

for x in shop.values():
    print(x)

#dipslaying the keys
for x in shop.keys():
    print(x)

#displaying both
for x,y in shop.items():
    print(x,y)

#exercise 5
teacher1 = {
  "name" : "Emilia",
  "subject" : "maths"
}
teacher2 = {
  "name" : "Tobias",
 "subject" : "chemistry"
}
teacher3 = {
  "name" : "Linus",
 "subject" : "english"
}

department = {
  "HEAD" : teacher1,
  "VICE" : teacher2,
  "NEW" : teacher3
}
print(department)

print(department["NEW"]["name"])



#integers
#x=7
#y=600000000
#z=-78
#print(x,y,z)
#print(type(x))
#print(type(y))
#print(type(z))


#floats
#a=5.4
#c=0.78888888
#b=-5.9
#print(type(a))
#print(type(c))
#print(type(b))

#complex numbers
#s=6 + 4j
#t=7j
#u=-3j
#print(type(s))
#print(type(t))
#print(type(u))

#type conversions exercise
s=6 + 4j
a=5.4
x=7
k="5.7"
z= complex(x)
print(z)

g=float(k)
print(g)
print(type(k))
print(type(g))



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