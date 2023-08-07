"""
#lists exercise
#1
Girls=["Carly","Kat","Tori","Trina","Jade"]
print(Girls[1])

#2
Girls[0]="Sam"
print(Girls)

#3
Girls.append("Carly")
print(Girls)

#4
Girls[2]="Bathel"
print(Girls)

#5
Girls.pop(3)
print(Girls)

#6
print(Girls[-1]) 

#7
num=[1,2,3,4,5,6,7]
print(num[2:5])

#8
country=["USA","UAE","UK"]
copy_made=country.copy()
print(copy_made)

#9
for x in country:
    print(x)

#10
animals=['cat','dog','baboon','eagle','cow']
animals.sort()
print(animals)

animals.sort(reverse=1)
print(animals)

#11
for x in animals:
    if 'a' in animals:
        print(x)

#12
phones=["samsung","infinix","iphone","tecno"]
old=["itel","nokia"]
technology=phones+old
print(technology)



#tuples exercise
#1
x=("samsung","iphone","tecno","redmi")
print(x[0])

#2
print(x[-2])

#3
x=("samsung","iphone","tecno","redmi")
y=list(x)
y[1]="itel"
z=tuple(y)
print(z)

#4
y.append("Huawei")
z=tuple(y)
print(z)

#5
for n in z:
    print(n)

#6
y.remove("samsung")
z=tuple(y)
print(z)

#7
cities=(["Kampala","Mbarara","Gulu","Mbale","Kasese"])
print(cities)

#8
cities=("Kampala","Mbarara","Gulu","Mbale","Kasese")
(central, south, north, east, west)=cities
print(central)

#9
print(cities[2:5])

#10
first_name=("Cronnie",)
x=list(first_name)
last_name=('Owomugisha','Angel')
y=list(last_name)
name= x + y
print(name)

#11
color=('green','red')
print(color*2)

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count=0
if count%8==0:
    print(count)
    ++count

#sets exercise
#1
drinks=set(("lemonade","tea", "water"))
print(drinks)

#2
additions={"milk", "yoghurt"}
drinks.update(additions)
print(drinks)

#3
mySet = {"oven", "kettle", "microwave", "refrigderator"}
if "microwave" in mySet:
 print("yes, I have one")
else:
 print("buy for me one")

#4
mySet.remove("kettle")
print(mySet)

#5
for x in mySet:
 print(x)

#6
phones={"samsung","infinix","iphone","tecno"}
laptops=["Macbook","Dell"]
laptops=set((laptops))
phones.union(laptops)
print(phones)

#7
names={'Saare','Timo','Dan'}
age={23,56,27}
person=names.union(age)
print(person)


#strings exercise
#1
name="Cronnie"
num=21
ans=name+ str(num)
print(ans)

#2
txt="   Hello,    Uganda     "
edit=txt.strip()
print(edit)

#3
print(txt.upper())

#4
print(txt.replace("U", "V"))

#5
y="I am proudly Ugandan"
print(y[2:5])

#6
#x = “All “Data Scientists” are cool!” 
x="All \"Data Scientists\" are cool!"
print(x)


#dictionaries

Shoes = {
"brand" : "Nike",
"color" : "black",
"size" : 40
}

#1
z=Shoes["size"]
print(z)

#2
Shoes["brand"]= "Adidas"
print(Shoes)

#3
Shoes.update({"type": "sneaker"})
print(Shoes)

#4
for x in Shoes.keys():
    print(x)

#5
for x in Shoes.values():
    print(x)

#6
if "size" in Shoes:
    print("we have the size")
else :
    print("sorry, unavailable")

#7
for x in Shoes:
    print(x)

#8
Shoes.pop("color")
print(Shoes)

#9
Shoes.clear()

#10
mydict={
"phone":"samsung",
"model":"S10",
"manufacturer":"android",
"colors": ["blue","red","green"]
}
new=mydict.copy()
print(new)

#11

child1 = {
  "name" : "Emilia",
  "DOB" : "12.03.09"
}
child2 = {
  "name" : "Tobias",
 "DOB" : "16.09.97"
}
wife = {
  "name" : "Linet",
 "DOB" : "12.12.79"
}

myfamily = {
  "wife" : wife,
  "first_born" : child2,
  "second_born" : child1
}
print(myfamily)

"""
