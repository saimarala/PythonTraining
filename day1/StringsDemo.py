# ways to create string
s = "welcome"
s = 'welcome'
s = str("welcome")
s = str('welcome')

# creation of empty strings
name = ""
name = ''
name = str()
# Example 2
# String is immutable
str1 = "welcome"
print(id(str1))  # 2383118771440
str1 = str1 + " to python"
print(id(str1))  # 2383119302576
# if values is not changed after updation then it is immutable

# Example 3 + and *
str = "welcome"
print(str + " to Python")

str = "welcome"
print(str * 10)

# Example 4 : slicing operator
str = "welcome"
print(str[1:4])  # elc
print(str[:4])  # starting index is 0 by default
print(str[2:])  # lcome
print(str[1:-1])  # elcom
print(str[1:-2])  # elco

# Example 5
# ord() and chr()

print(ord("A"))  # 65
print(chr(99))  # c

# Example 6

# max() min() and len()
print(min("Abc"))  # A
print(max("Abc"))  # c
print(len("Python"))  # 6

# Example 7 in not in operators
s = "welcome to python"
print("python" in s)  # True
print("java" in s)  # False
print("python" not in s)  # False
print("java" not in s)  # True

# Example 8 String comparison
print("tim" == "tie")  # False
print("free" != "freedom")  # True
print("arrow" > "aron")  # True
print("right" >= "left")  # True
print("teeth" < "teet")  # False
print("yellow" <= "fellow")  # False
print("abc" > "")  # True
print("tim" == "tie")  # False

# Example 9 testing String True/False
s = "welcome to python"
print(s.isalnum())  # False
print("welcome".isalpha())  # True
print("2013".isdigit())  # True
print("first number".isidentifier())  # False
print(s.islower())  # True
print("SAI".isupper())  # True
print(" ".isspace())  # True

# Examples for searching substrings
print("***substrings**")
s = "welcome to python"
print(s.endswith("hon"))  # True
print(s.startswith("hai"))  # False
print(s.find("me"))  # 5
print(s.find("sai"))  # -1 not found
print(s.count("o"))  # 3 returns the number of occurrences od substring of string

# Examples 11: converting string
s = "String is in PYTHON"
print(s.capitalize())  # String is in python
print(s.title())  # String Is In Python
print(s.lower())  # string is in python
print(s.upper())  # STRING IS IN PYTHON
print(s.swapcase())  # sTRING IS IN python
print(s.replace("in", "on"))  # Strong is on PYTHON

# Example 12: reverse string
# Method1
s = "welcome"
rev_str = ""
for i in s:
    rev_str = i + rev_str
print(rev_str)  # emoclew
# method 2
s = "welcome"
rev_str = s[::-1]
print(rev_str)  # emoclew
