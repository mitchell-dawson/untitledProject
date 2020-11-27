from projectName import module1 # load module from top level
c1 = module1.Class1()

from projectName import Class1 # load object from top level module directly
c1_extra = Class1()

from projectName.subpackage_1 import moduleB # load module from subpackage
b1 = moduleB.ClassB1()
b2 = moduleB.ClassB2()

from projectName.subpackage_1 import ClassA # load object from subpackage module
cA = ClassA()

from projectName import ClassC  # load object from subpackage module directly
cC = ClassC()