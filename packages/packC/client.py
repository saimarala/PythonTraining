import sys

sys.path.append("D:/AutomationLabs/PythonTraining/packages/packA")
sys.path.append("D:/AutomationLabs/PythonTraining/packages/packB")

# #Approach1:
# import  emp
# empObj=emp.Employee(101,"Python",2000)
# empObj.displayemp()#101 Python 2000
#
# import  stu
# empObj=stu.Student(22,"Python","A")
# empObj.displaystu()#22 Python A

# Approach2:
from emp import Employee

empObj = Employee(101, "Python", 5000)
empObj.displayemp()  # 101 Python 5000

from stu import *

stuObj = Student(1, "Python student", 'A')
stuObj.displaystu()  # 1 Python student A
