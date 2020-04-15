import unittest
from numberTriangles2 import largestSum

class numberTrianglesTest(unittest.TestCase):
  def test_1(self):
    result = largestSum([
    [],
    [7], 
    [3, 8], 
    [8, 1, 0], 
    [2, 7, 4, 4], 
    [4, 5, 2, 6, 5]], 5)
    self.assertEqual(result, 30)

if __name__ == '__main__':
  unittest.main()