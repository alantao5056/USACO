import unittest
from is_90_rotate import is90Rotate

class Is90RotateTest(unittest.TestCase):
  def test_1(self):
    original = [['@', '-', '@'], ['-', '-', '-'], ['@', '@', '-']]
    transformed = [['@', '-', '@'], ['@', '-', '-'], ['-', '-', '@']]
    result = is90Rotate(3, original, transformed)
    self.assertTrue(result, True)

if __name__ == "__main__":
  unittest.main()