# Example1:
# print("this is starting point of program...")
# print("this is starting point of program...")
# print("this is starting point of program...")
#
# try:
#     print(x)
# except:
#     print("Exception is occured")
#
# print("this is end of program..")
# print("this is end of program..")
# print("this is end of program..")
# Example2:
print("This is starting point of program...")
print("Program in progress")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Exception occured..handled")
print("program completed..")

# Example3:Multiple exception - try, except else, finally
try:
    num1, num2 = 10, 0
    result = num1 / num2
    print("result is ", result)
except ZeroDivisionError:
    print("Thrown zero division exception...")
except SyntaxError:
    print("Thrown syntax error exception..")
except:
    print("Exception handled..")
else:
    print("No exceptions occured..")
finally:
    print("finally always execute...")
#Exception4:raising own exception
def enterage(num):
    if num<0:
     raise ValueError("only Integers are allowed")
    if num%2==0:
        print("even number")
    else:
        print("odd number")
print("checking number is even or odd by calling function..")
num=-1
try:
    enterage(num)
except ValueError:
    print("value error exception occurred and handled")
print("program completed..")
