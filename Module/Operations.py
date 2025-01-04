# Approach1
from Module import calculator

calculator.add(100, 200)  # 300
calculator.mul(10, 20)  # 200
# Approach2
# from calculator import add,mul
# add(1,2)#3
# mul(2,3)#6
# Approach3
from Module.calculator import *

add(1, 2)  # 3
mul(2, 3)  # 6
