# Eamcpale 1 how to create list
myList1 = [10, 20, 30, 40, 50]
myList2 = ["Apple", "Banana", "Mango"]
myList3 = ["apple", 10, "banana", True]
myList = list()
print(myList1)
print(myList2)
print(myList3)
print(myList)

# Example2 : Accessing items from the list
myList = ["Apple", "Banana", "Mango"]  # index starts from zero
print(myList[0])  # Apple
print(myList[2])  # Mango
print(myList[-1])  # Mango
print(myList[-2])  # Banana

# Example3 : Range of indexes
myList = ["apple", "banana", "cherry", "orange", "kiwi", "lemon", "mango"]
print(myList[2:5])  # ['cherry', 'orange', 'kiwi']
print(myList[-4:-1])  # ['orange', 'kiwi', 'lemon']

# Example4: change the item value

myList = ["apple", "banana", "cherry"]
print(myList)  # ['apple', 'banana', 'cherry']
myList[0] = "mango"  # this change the value based index
print(myList)  # ['mango', 'banana', 'cherry']

# Example5: read the list items using loop
myList = ["apple", "banana", "cherry"]
for i in myList:
    print(i)  # apple banana cherry

# Example6: check item is exist in the list ot not
myList = ["apple", "banana", "cherry"]
if "apple" in myList:
    print("yes apple is present")
else:
    print("no apple is present")
# Example7:List length
myList = ["apple", "banana", "cherry"]
print(len(myList))  # 3

# Example8 : add items append() insert()
myList = ["apple", "banana", "cherry"]
# myList.append("orange")# adding new item at end of the lis
# print(myList)#['apple', 'banana', 'cherry', 'orange']
myList.insert(1, "orange")  # adding item some where in the middle of the list based on the index
print(myList)  # ['apple', 'orange', 'banana', 'cherry']

# Example9 :remove item from the list
myList = ["apple", "banana", "cherry"]
myList.pop(0)  # here we should specify the index not value
print(myList)  # ['banana', 'cherry']
# del
myList = ["apple", "banana", "cherry"]
del myList[1]  # del command renove the single item based on the index
print(myList)  # ['apple', 'cherry']
# clear
myList = ["apple", "banana", "cherry"]
myList.clear()
print(myList)  # []

# Example10 : copy list
# list()
myList1 = ["apple", "banana", "cherry"]
myList2 = list(myList1)
print(myList1)  # ['apple', 'banana', 'cherry']
print(myList2)  # ['apple', 'banana', 'cherry']
# copy
myList1 = ["apple", "banana", "cherry"]
myList2 = myList1.copy()
print(myList1)  # ['apple', 'banana', 'cherry']
print(myList2)  # ['apple', 'banana', 'cherry']

# Example11: combine/join the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # ['a', 'b', 'c', 1, 2, 3]

# using loop statment
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for i in list2:
    list1.append(i)
print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# using extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # ['a', 'b', 'c', 1, 2, 3]
