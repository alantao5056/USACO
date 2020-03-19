import unittest
from isReflection import isReflection

class isReflectionTest(unittest.TestCase):
  def test_1(self):
    original = ['@-@', '--@', '-@-']
    transformed = ['@-@', '@--', '-@-']
    self.assertTrue(isReflection(3, original, transformed), True)
  
  def test_2(self):
    original = ['@-@-', '@@-@', '@@@-', '-@@@']
    transformed = ['-@-@', '@-@@', '-@@@', '@@@-']
    self.assertTrue(isReflection(4, original, transformed), True)

  def test_3(self):
    original = ['@--', '@@@', '--@']
    transformed = ['@@@', '@@-', '--@']
    self.assertFalse(isReflection(3, original, transformed), False)

if __name__ == '__main__':
  unittest.main()