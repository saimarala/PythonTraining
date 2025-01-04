#Approach1:
# import A
# import B
# obj1=A.Animal()
# obj1.display()#I like cow
#
# obj2=B.Bird()
# obj2.display()#I like parrot

#Approach2:
from A import Animal
from B import Bird
obj1=Animal()
obj1.display()#I like cow
obj2=Bird()
obj2.display()#I like parrot