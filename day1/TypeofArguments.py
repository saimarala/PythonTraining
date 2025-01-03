# Example1:

def func(i, j):
    print(i, j)


func(10, 20)  ##10 20 positional arguments
func(j=20, i=10)  # 10 20 # Keyword arguments


# Example2: default values assigned to positional arguments
def func(i, j=10):
    print(i, j)


func(100, 200)  # 100 200
func(100)  # 100 10


# Example3: keyward arguments
def greetings(name, greetmsg):
    print(greetmsg + " " + name)


greetings(name="Python", greetmsg="Hello")  # Hello Python
greetings(greetmsg="Hello", name="Python")  # Hello Python


# Example4:
def my_func(a, b, c):
    print(a, b, c)


my_func(10, 30, 30)  # positional arguments
my_func(a=10, b=20, c=30)  # Keyword arguments
my_func(b=20, a=10, c=30)  # Keyword arguments

my_func(10, 20, c=30)
my_func(10, b=20, c=30)


# my_func(10,b=20,30)#this is wrong as positional argument must appear before any keyword argument
# my_func(10,30,b=20)#TypeError: my_func() got multiple values for argument 'b'

# Example 5:
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(100, 200))
res = (largest(10, 20))
print(type(res))  # <class 'tuple'>
