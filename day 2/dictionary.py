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