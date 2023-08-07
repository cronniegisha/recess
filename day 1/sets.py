#it is unordered, unchangeable and unindexed
phones={"samsung","infinix","iphone","tecno"}
print(phones)

#dupliates are not allowed
phones={"samsung","infinix","iphone","tecno","infinix"}
print(phones)

#lenth of a set
print(len(phones))

#type of a set
print(type(phones))

#accessing items in a set
#NO INDEXING
#using a loop
phones={"samsung","infinix","iphone","tecno"}
for x in phones:
 print(x)

#using in
print("samsung" in phones)

#adding items
phones.add("sony")
print(phones)

#adding sets 
# using update
#when using update it doesnt necessarily have to be a set, it can be a tuple,list
phones={"samsung","infinix","iphone","tecno"}
old={"itel","nokia"}
phones.update(old)
print(phones)

#using union
phones={"samsung","infinix","iphone","tecno"}
old={"itel","nokia","blackberry"}
gadgets=phones.union(old)
print(gadgets)


#we remove items using the discard() or remove() method
phones.remove("iphone")
print(phones)
#print(phones.discard("tecno"))#returns NONE

#pop() removes a randomitem and returns the item that has been popped
#yu dont know which item gets removed
x=phones.pop()
print(x)

#clear( )empties the set
phones.clear()
print(phones)

#del() deletes the set
del phones
#print(phones)