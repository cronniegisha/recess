#Lists
# They are changeable and ordered. they also allow duplicates.
#Girls=["Martya","Arizona","Sarah"]
#print(Girls)

#duplicates in lists
Girls=["Martya","Arizona","Sarah","Arizona","Sarah"]
print(Girls)

#list length
print(len(Girls))

#list type
print(type(Girls))

#access list
print(Girls[0]) #prints Martya
print(Girls[1:3])# prints a range of data in those indices
print(Girls[-2]) #prints Arizona
print(Girls[:4])# this excludes the last item

#using the set() constructor this is to make the list a set
Girls= set(("Kellen","Sarah"))
print(Girls)

#turples
#they are unchangeable, ordered and allow duplicates
#in order to change items in a turple make it a list


