# print 1..10 numbers using for loop

for i in range(10):
    print(i)  # 0...9

for i in range(1, 11):
    print(i)  # 1...10

# print only even numbers
for i in range(2, 21, 2):
    print("even:", i)
# print only odd numbers
for i in range(1, 21, 2):
    print("odd :", i)
# print only odd numbers in descending order (10,9,8......1)

for i in range(10, 0, -1):
    print(i)
# print 5,10,15
for i in range(5, 101, 5):
    print(i)
