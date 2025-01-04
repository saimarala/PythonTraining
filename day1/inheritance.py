# Example1: single inheritance
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
# boobj=B()
# boobj.m1()#this is m1 method from class A
# boobj.m2()#this is m2 method from class B

# Example2: single inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
# bobj=B()
# bobj.m1()#30
# bobj.m2()#-100
# #Example 3: Multilevel inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
# class C(B):
#     i,j=5,2
#     def m3(self):
#      print(self.i*self.j)
#
# cobj=C()
# cobj.m1()#30
# cobj.m2()#-100
# cobj.m3()#10
# Example 4: Hierarchy inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
# class C(A):
#     i,j=5,2
#     def m3(self):
#      print(self.i*self.j)
#
# bobj=B()
# bobj.m1()#30
# bobj.m2()#-100
# cobj=C()
# cobj.m1()#30
# cobj.m3()#10

# Example 5: Hierarchy inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#      print(self.i*self.j)
#
#
# cobj=C()
# cobj.m1()#30
# cobj.m2()#-100
# cobj.m3()#10

# Example6 : calling parent class method using child class using super()
# class A:
#     def m1(self):
#         print("This m1 method from class A")
# class B(A):
#     def m1(self):
#         print("This m2 method from class B")
#         super().m1()
#
# bobj=B()
# bobj.m1()#print("This m2 method from class B")
# This m1 method from class A

# Example7 :
# class A:
#     a, b = 10, 20
#
#
# class B(A):
#     i, j = 100, 200
#     def m(self, x, y):
#         print(x + y)  # local varaiables 30
#         print(self.i + self.j)  # class variables 300
#         print(self.a + self.b)  # class variables 30
# bobj = B()
# bobj.m(10, 20)

# Example8 :overriding variables
#
# class Parent:
#     name="Python"
# class Child(Parent):
#     name="Testing"#overriding the variable
#     def test(self):
#         print(super().name)
#
# cobj=Child()
# print(cobj.name)#Testing
# t=cobj.name
# print(t)#Testing
# cobj.test()#Python


# Example9: overriding methods
# class Bank:
#     def roi(self):
#         return 0
# class XBank(Bank):
#     def roi(self):
#         return 10
# class YBank(Bank):
#     def roi(self):
#         return 12
# objx=XBank()
# print(objx.roi())#10
# objy=YBank()
# print(objy.roi())#12

# Example10 : overloading
# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello")
# h = Human()
# h.sayHello()
# h.sayHello("Python")
# Example11 : overloading2

class cal:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


cObj1 = cal()
cObj1.add()  # 0
cObj1.add(10, 20)  # 30
cObj1.add(10, 20, 30)  # 60
