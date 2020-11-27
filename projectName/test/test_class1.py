import unittest
from projectName import Class1

class Mock_Class1():

    def __init__(self):
        pass

    def get_Class1(self):
        return Class1()

class Test_Class1(unittest.TestCase):

    def test_repr_Class1(self):

        class1 = Class1()
        self.assertEqual(str(class1), "Class1")

if __name__ == '__main__':
    unittest.main()