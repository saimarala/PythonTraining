# Example1 : creating dictionary
myDic = {101: "x", 102: "y", 103: "z"}
print(myDic)

# Example2 : accessing item from dictionary
myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
print(myDic["year"])  # 2020

# using get()
print(myDic.get("brand"))  # Hyundai
x = (myDic.get("model"))
print(x)  # i10

# Example3: change values in the dictionary
myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
print(myDic)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020}
myDic["year"] = 2021
print(myDic)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}

# Example4: reading items from dictionary using loop
myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
for i in myDic:
    print(i)  # print only keys from dictionary
for i in myDic:
    print(myDic[i])  # print only values from dictionary
for i in myDic.values():
    print(i)  ##print only values from dictionary

for x, y in myDic.items():
    print(x, y)  # print keys and values from dictionary
#
# Example5: check key exists in dictionary or not
myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
if "model" in myDic:
    print("exist")
else:
    print("not exist")

print("model" in myDic)  # True

# Example6 : find number of items in dictionary

myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
print(len(myDic))  # 3
# Example7 : Add item to the dictionary
myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}

myDic["color"] = "red"
print(myDic)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020, 'color': 'red'}

# Example8 :remove item from dictionary
myDic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
# myDic.pop("year")
# print(myDic)#{'brand': 'Hyundai', 'model': 'i10'}
del myDic["model"]
print(myDic)  # {'brand': 'Hyundai', 'year': 2020}

# del myDic
# print(myDic)#NameError: name 'myDic' is not defined
myDic.clear()
print(myDic)  # {}

# Example9 : copying dcitionary

myDic1 = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
# copy
myDic2 = myDic1.copy()
print(myDic2)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020}
# without using copy
# myDic2=myDic1
# print(myDic2)#{'brand': 'Hyundai', 'model': 'i10', 'year': 2020}
