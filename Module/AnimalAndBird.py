# Appraoch1:
import Animal
import Bird

Animal.fly()
Animal.color()

Bird.fly()
Bird.color()

# Appraoch2:
from Animal import *
from Bird import *

# will invoke the latest imports
fly()  # Bird can fly
color()  # Bird is green

from Animal import *

fly()  # Animal can't fly
color()  # Animal is Black
from Bird import *

fly()  # Bird can fly
color()  # Bird is green
