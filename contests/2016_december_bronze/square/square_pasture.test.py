import unittest
from square_pasture import main

class squareTest(unittest.TestCase):
  
  testDataFolder = 'test_data'  
    
  def do_test(self, testNumber):
    testFile = self.testDataFolder + "/" + str(testNumber)
    main(testFile + ".in", testFile + "_actual.out")
    # compare the result
    expectedOut = open(testFile + ".out", 'r')
    actualOut = open(testFile + "_actual.out", 'r')
    expectedLines = expectedOut.readlines()
    actualLines = actualOut.readlines()
    expectedOut.close()
    actualOut.close()
    self.assertEqual(actualLines, expectedLines)
  
def generate_test(testNumber):
  def test(self):
    self.do_test(testNumber)
  return test

if __name__ == '__main__':
  for i in range(1, 11):
    test_name = 'test_%s' % str(i)
    test = generate_test(i)
    setattr(squareTest, test_name, test)
  unittest.main()
  

  # def test_1(self):
  #   square_1 = [6, 6, 8, 8]
  #   square_2 = [1, 8, 4, 9]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 49)

  # def test_2(self):
  #   square_1 = [5, 8, 6, 9]
  #   square_2 = [2, 1, 9, 7]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 64)

  # def test_3(self):
  #   square_1 = [8, 1, 9, 4]
  #   square_2 = [3, 4, 6, 7]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 36)

  # def test_4(self):
  #   square_1 = [5, 0, 7, 2]
  #   square_2 = [0, 1, 3, 3]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 49)

  # def test_5(self):
  #   square_1 = [3, 0, 5, 8]
  #   square_2 = [1, 1, 2, 7]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 64)

  # def test_6(self):
  #   square_1 = [0, 1, 3, 4]
  #   square_2 = [5, 0, 6, 10]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 100)

  # def test_7(self):
  #   square_1 = [1, 3, 2, 6]
  #   square_2 = [4, 1, 8, 5]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 49)

  # def test_8(self):
  #   square_1 = [1, 2, 7, 3]
  #   square_2 = [8, 2, 10, 4]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 81)

  # def test_9(self):
  #   square_1 = [2, 2, 5, 7]
  #   square_2 = [9, 6, 10, 8]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 64)

  # def test_10(self):
  #   square_1 = [4, 0, 7, 1]
  #   square_2 = [1, 6, 7, 8]
  #   x = [square_1[0], square_1[2], square_2[0], square_2[2]]
  #   y = [square_1[1], square_1[3], square_2[1], square_2[3]]
  #   self.assertEqual(getLength(x, y), 64)

