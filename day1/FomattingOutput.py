# name="Python"
# age=30
# sal=5000.50
# Approach1
name, age, sal = "Python", 30, 500.50
print(name, age, sal)

# Approach2
print("Name is :", name)
print("Age is:", age)
print("Sal is:", sal)

# Approach3
print("Name is:%s Age is:%d Salary is:%g" % (name, age, sal))  # Name is:Python Age is:30 Salary is:500.5
# Approach4
# order is also most important
print("Name is:{} Age is:{} Salary is:{}".format(name, age, sal))  # Name is:Python Age is:30 Salary is:500.5
