import unittest
from primePalindromes2 import toString

class toStringTest(unittest.TestCase):
  def test_1(self):
    self.assertEqual(toString(2, 2), '02')

  def test_2(self):
    self.assertEqual(toString(1234, 3), '1234')

  def test_3(self):
    self.assertEqual(toString(1234, 6), '001234')

  def test_4(self):
    self.assertEqual(toString(1234, 4), '1234')

  def test_5(self):
    self.assertEqual(toString(0, 0), '0')

if __name__ == '__main__':
  unittest.main()