import unittest
from mothersMilk import getComb

class mothersMilkTest(unittest.TestCase):

  def test_1(self):
    self.assertTrue(getComb(3, 2, 1), '0 1\n')

  def test_2(self):
    self.assertTrue(getComb(2, 3, 1), '0 1\n')

  def test_3(self):
    self.assertTrue(getComb(3, 1, 2), '1 2\n')

  def test_4(self):
    self.assertTrue(getComb(8, 9, 10), '1 2 8 9 10\n')
  
  def test_5(self):
    self.assertTrue(getComb(2, 5, 10), '5 6 7 8 9 10\n')
if __name__ == '__main__':
  unittest.main()