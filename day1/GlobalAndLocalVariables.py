#
# Global and local variables
# The variables create outside of the function are called global varaibles
# The variables create inside of the function are called local varaibles

# Example1:
global_var = 20  # global variable


def fun():
    local_var = 10  # local variable
    print(local_var)  # 30
    print(global_var)  # 30


fun()  # 10 20
# print(local_var)#invalid bcoz local_var is local variable of func()
print(global_var)  # valid bcoz global_var is a global variable

# Example2:
xy = 100


def cool():
    xy = 200
    print(xy)


cool()  # 200
print(xy)  # 200

# Example3:
xy = 100


def cool():
    # global xy=200 #invalid
    global xy
    xy = 200  # global varaible
    print(xy)


cool()  # 200
print(xy)  # 200

# Example4:
x = 100


def cool():
    global x
    x = 500
    print(x)


cool()  # 500
print(x)  # 500


# Example4:
def cool():
    global x
    x = 400
    print(x)


cool()  # 400
print(x)  # 400 able access bocoz it is global variables
