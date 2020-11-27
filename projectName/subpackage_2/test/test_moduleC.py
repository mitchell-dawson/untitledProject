import unittest
from projectName.subpackage_1 import ClassA
from projectName.subpackage_2 import moduleC

class TestModuleC(unittest.TestCase):

    def test_output_ClassAFactory(self):

        self.assertTrue(
            isinstance(moduleC.ClassAFactory().output, ClassA))

if __name__ == '__main__':
    unittest.main()


