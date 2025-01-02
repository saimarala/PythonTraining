# Example1 : how to create tuple
from day1.ListDemo import myList

myTuple = ("Apple", "banana", "cheery")
print(myTuple)  # ['Apple', 'banana', 'cheery']
myTuple = ()  # empty tuple
# Example2 : access tuple items
myTuple = ("Apple", "banana", "cheery")
print(myTuple[1])  # banana index starts from 0
print(myTuple[-1])  # cheery
# Example3 : range of indexes
myTuple = ("apple", "banana", "cherry", "orange", "kiwi", "lemon", "mango")
print(myTuple[2:5])  # ['cherry', 'orange', 'kiwi']
print(myTuple[-4:-1])  # ['orange', 'kiwi', 'lemon']

# Example 4 change the tuple items
# 1.we cannot add existing value
# 2.we cannot append the new value
# 3.we cannot insert the new value
# 4.we cannot remove a value
# immutable but there is work around
# tuple -->list -->tuple
myTuple = ("Apple", "banana", "cheery")
myList = list(myTuple)
myList[0] = "orange"
myTuple = tuple(myList)
print(myTuple)  # ('orange', 'banana', 'cheery')
# Example 5: using tuple
myTuple = ("Apple", "banana", "cheery")

for i in myTuple:
    print(i)  # Apple  banana cheery

# Example 6: check if item exists
myTuple = ("Apple", "banana", "cheery")
if "banana" in myTuple:
    print("banana is present")
else:
    print("no,baana")

# Example7:len
myTuple = ("Apple", "banana", "cheery")
print(len(myTuple))  # 3
# Example8:add items to the tuple no possible because of immutable
myTuple = ("Apple", "banana", "cheery")
# myTuple[0]="orange"#type error
print(myTuple)

# Example9: copy tuple
myTuple1 = ("Apple", "banana", "cheery")
myTuple2 = myTuple1
print(myTuple2)  # ('Apple', 'banana', 'cheery')

# Example10: remove not possible bcoz immutable
myTuple = ("Apple", "banana", "cheery")
# myTuple.remove("banana") #invlaid
# del  myTuple#not valid
print(myTuple)  # NameError: name 'myTuple' is not defined

# Example11,: joining/combine
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 'a', 'b', 'c')

# Example 12
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
if tuple1 == tuple3:
    print("equal")
else:
    print("!=")
