import unittest
from is_270_rotate import is_270_rotate

class is270RotateTest(unittest.TestCase):
  def test_1(self):
    original = ['@-@', '--@', '-@-']
    transformed = ['@@-', '--@', '@--']
    self.assertTrue(is_270_rotate(3, original, transformed), True)

  def test_2(self):
    original = ['@@--', '@-@@', '@@@@', '-@@-']
    transformed = ['-@@-', '-@@@', '@-@@', '@@@-']
    self.assertTrue(is_270_rotate(4, original, transformed), True)
  
  def test_3(self):
    original = ['@@--', '@---', '@@@@', '@-@@']
    transformed = ['@@@@', '@---', '----', '---@']
    self.assertFalse(is_270_rotate(4, original, transformed), False)

if __name__ == '__main__':
  unittest.main()
