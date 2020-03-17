import unittest
from isCombination import isCombination

class isCombinationTest(unittest.TestCase):
  def test_1(self):
    original = ['@-@-', '@@-@', '@@@-', '-@@@']
    rotated = ['@-@-', '@@-@', '@@@-', '-@@@']
    self.assertTrue(isCombination(4, original, rotated), True)

  def test_2(self):
    original = ['@@-', '@@@', '--@']
    rotated = ['@@-', '@-@', '@@-']
    self.assertFalse(isCombination(3, original, rotated), False)

if __name__ == '__main__':
  unittest.main()