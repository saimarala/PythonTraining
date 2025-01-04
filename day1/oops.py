# Example1:

class myClass:
    def myfun(self):  # bydefault every method will take one argument as a self
        pass

    def display(self):
        print("Python")

    def display1(self, name):
        print(name)


myClass().display()  # Python
mc1 = myClass()
mc2 = myClass()
mc1.myfun()
mc2.display()  # Python
mc2.display1("test")


# Example2:
class myclass:
    def m1(self):  # representing the class
        print("instance method")

    @staticmethod
    def m2(self, num):  # self expecting in one parameter
        print(self, num)


mc = myclass()
mc.m1()
# mc.m2(100)#TypeError: mycalss.m2() missing 1 required positional argument: 'num'
mc.m2(100, 200)  # 100 200

myclass().m2(100, 200)  # 100 200


# Example3:
class myClass:
    a, b = 10, 20  # class variables

    def add(self):
        print(self.a, self.b)

    def mul(self):
        print(self.a * self.b)


mc = myClass()
mc.add()  # 10 20
mc.mul()  # 200

# Example4:
i, j = 15, 25  # global variables


class myClass1:
    a, b = 10, 20  # class variables

    def add(self, x, y):  # x,y local variables
        print(x + y)  # x,y are local varaiables
        print(self.a + self.b)  # a,b are class variables
        print(i + j)  # i,j are global variables


mc1 = myClass1()
mc1.add(100, 200)  # 300 30 40

# Example5:
a, b = 15, 25  # global variables


class myClass2:
    a, b = 10, 20  # class variables

    def add(self, a, b):  # x,y local variables
        print(a + b)  # local
        print(self.a + self.b)  # class
        print(globals()['a'] + globals()['b'])  # global


mc2 = myClass2()
mc2.add(100, 200)  # 300 30 40


# Example6: once class have multiple objects
class Myclass3:
    def display(self, name):
        print("this is display method...")
        print(name)


mc3 = Myclass3()
mc3.display("test")
mc4 = Myclass3()
mc4.display("python")


# Example7 : constructor example
class MyClass4:
    def __init__(self):
        print("this is constructor")

    def m1(self):
        print("hello")

    def m2(self, x, y):
        return (x + y)


obj = MyClass4()  # invoke the constructor automatically
obj.m1()  # method we have call explicitly using object
print(obj.m2(1, 2))  # 3
res = obj.m2(10, 20)
print(res)  # 30


# Example8 :
class Myclass4:
    name = "test"

    def __init__(self, name):  # constructor expecting one argument
        print(name)
        print(self.name)


obj4 = Myclass4("Python")  # Python test  passing parameter to constructor


# Example9:
class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print(self.eid, self.ename, self.sal)


e1 = Emp(101, "test", "2000")
e1.display()  # 101 test 2000
e2 = Emp(102, "test1", "3000")
e2.display()  # 102 test1 3000


# Example10:
class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):
        return (self.ename)
    # return (self.ename,self.sal)#invalid becoz __str__(self) return only string value


e1 = Emp(103, "test3", "3000")
print(e1)
e2 = Emp(104, "test4", "4000")
print(e2)
