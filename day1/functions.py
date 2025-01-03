# Functions
# Function means set of statements which will perform task
# 1.function declration/creation
# 2.calling the function/invoking function
# function does not take argumnets not return any value
# function does not take argumnets but return any value
# function does take argumnets not return any value
# function does take argumnets and also return any value
# #Example1

def myfun():
    print("hellO")  # hellO
myfun()  # call the function

# Example2:
def myfun(name):
    print("Hello", name)  # Hello python

myfun("python")

# Example3 :
def myfunc(a, b):
    return (a + b)


sum = myfunc(10, 30)
print(sum)  # 40
print(myfunc(100, 200))  # 300


# Example4 :
def myfunc1():
    return


print(myfunc1())  # None


def myfunc1():
    i = 10


print(myfunc1())  # None


# Example5 :
def cal(a, b):
    print(a + b)


cal(10, 20)  # 30


def cal1(a, b):
    return print(a + b)


cal1(10, 20)  # 30
