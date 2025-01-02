# range : values between range

print(range(10))  # print(range(10))#
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 10)))  # [5, 6, 7, 8, 9]

# print only odd numbers
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
# print only even numbers
print(list(range(2, 20, 2)))  # [2, 4, 6, 8, 10, 12, 14, 16, 18]

print(list(range(10, 1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(-10, -5)))  # [-10, -9, -8, -7, -6]
print(list(range(-10, -5, 2)))  # [-10, -8, -6]
