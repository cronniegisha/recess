#a turple is used to store multiple items in a single variable
#it is ordered and unchangeable
fruits=("apples","bananas","grapes")
print(fruits)

#they allow duplicates
fruits=("apples","bananas","grapes","apples")
print(fruits)

#also uses the len() function for length

fruits=("apples",)
print(type(fruits))#this is a turple

fruits=("apples")
print(type(fruits))#this is a string

fruits=("grapes", True, 0.5, 2)
print(type(fruits))#this is also a turple

#acessing items in a turple
print(fruits[1])
#negative indexing means we start from the end

print(fruits[:2])#from the beginning but not including the index2

#to determine presence of an item we use "in"
fruits=("apples","bananas","grapes","apples")
if "mango" in fruits:
 print("yes, i have a mango")
else:
 print("buy for me one")

 #in order to change things in a turple change it to a list and then back
 fruits=("apples","bananas","grapes","apples")
 listedfruits=list(fruits)
 listedfruits[3]="kiwi"
 fruits=tuple(listedfruits)
 print(fruits)

 #using the append() and remove()
 fruits=("apples","bananas","grapes","apples")
 listedfruits=list(fruits)
 listedfruits.append("oranges")
 listedfruits.remove("bananas")
 fruits=tuple(listedfruits)
 print(fruits)

 #adding tuples and deleting some
 fruits=("apples","bananas","grapes","apples")
 listedfruits=("lemons",)
 fruits+=listedfruits
 print(fruits)
 del listedfruits
 #print(listedfruits)#generates error
 
 #packing and unpacking varibles
 #Packing is assigning values to a tuple
 #unpacking is extacting values back into variables
 fruits=("apples","bananas","grapes",)
 (green, yellow, red)=fruits
 print(red)

#using the asterix(this is used when the values are more than the variables)
 fruits=("apples","bananas","grapes","tomato",)
 (green, yellow, *red)=fruits
 print(red)
 





