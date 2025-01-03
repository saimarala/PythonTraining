#Example1 : creating set
mySet={"apple","banana","cheery"}
print(mySet)

#Example2 : Accessing items from set
mySet={"apple","banana","cheery"}
for i in mySet:
    print(i)#cheery apple banana

 ##Example3 :value exist set or not
mySet = {"apple", "banana", "cheery"}
print("banana" in mySet)#True
print("mango" in mySet)#False

#Example4 : Adding item to set
#add()- single item update() multiple items
mySet = {"apple", "banana", "cheery"}
mySet.add("orange")
print(mySet)#{'banana', 'cheery', 'orange', 'apple'}

mySet.update(["manago","kiwi","lemon"])
print(mySet)#{'kiwi', 'banana', 'orange', 'cheery', 'apple', 'lemon', 'manago'}

#Example5 : find number of items

mySet = {"apple", "banana", "cheery"}
print(len(mySet))#3

#Example6 : remove() and discard
mySet = {"apple", "banana", "cheery"}
# mySet.remove("banana")
# print(mySet)#{'apple', 'cheery'}
#mySet.remove("mango")#KeyError: 'mango'
print(mySet)
mySet.discard("banana")
print(mySet)#{'cheery', 'apple'}
mySet.discard("mango")#will not throw any error
print(mySet)

#Example7 : clear all the items from set
mySet = {"apple", "banana", "cheery"}
mySet.clear()
print(mySet)#set()

# del mySet
# print(mySet)#NameError: name 'mySet' is not defined

#Example8 : joining the two sets -union
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)#{'a', 1, 2, 3, 'c', 'b'}
#update
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)#{1, 2, 3, 'a', 'c', 'b'}
