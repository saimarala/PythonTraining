#Approach1:
# import sys
# sys.path.append("D:/AutomationLabs/PythonTraining/packages/package1")
# sys.path.append("D:/AutomationLabs/PythonTraining/packages/package1/package2")
# import Module1
# import Module2
# Module1.display()#Display function from module1
# Module2.show()#Show function from module2

#Approcah2:
import sys
sys.path.append("D:/AutomationLabs/PythonTraining/packages/package1")
sys.path.append("D:/AutomationLabs/PythonTraining/packages/package1/package2")

from Module1 import *
from Module2 import *
display()#Display function from module1
show()#Show function from module2


