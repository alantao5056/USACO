import unittest
from primePalindromes2 import isPrime

class isPrimeTest(unittest.TestCase):
  def test_1(self):
    self.assertTrue(isPrime(10301))
    
  def test_2(self):
    self.assertTrue(isPrime(2))

  def test_3(self):
    self.assertFalse(isPrime(4))

if __name__ == '__main__':
  unittest.main()
  