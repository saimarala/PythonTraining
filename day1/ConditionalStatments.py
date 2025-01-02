# Conditional statments
# if if..else elif

# Example1  : Print the person eligible for vote
age = 15

if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# Example2
if True:
    print("true conditon")
else:
    print("false condition")

# Example3
if 1:
    print("one")
else:
    print("zero")

# Example 4 : Find a number is even/odd
num = 10
if num % 2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")

# Example 5 ternary operator

num = 10
print("Even number") if num % 2 == 0 else print("odd number")

# Example 6 if else - multiple statments in single line
a = 20
{print("hello"), print("python")} if a > 10 else {print("hi"), {print("java")}}

# Example 7 multiple conditions

weekno = 1

if weekno == 1:
    print("sunday")
elif weekno == 2:
    print("momday")
elif weekno == 3:
    print("tuesday")
elif weekno == 4:
    print("wednesday")
elif weekno == 5:
    print("thrusday")
elif weekno == 6:
    print("friday")
elif weekno == 7:
    print("saturday")
else:
    print("invalid week number")
