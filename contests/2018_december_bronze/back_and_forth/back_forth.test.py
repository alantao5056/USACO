import unittest
from back_forth import getAllPossibleComb

class backForthTest(unittest.TestCase):
  def test_1(self):
    self._test(1)
  def test_2(self):
    self._test(2)
  def test_3(self):
    self._test(3)

  def _test(self, index):
    inFile = "test_data/" + str(index) + ".in"
    outFile = "test_data/" + str(index) + ".out"
    # read input
    inputAnswer = open(inFile)
    # getAllPossibleComb
    result = getAllPossibleComb(inputAnswer.readline().strip().split(), inputAnswer.readline().strip().strip())
    # read output
    output = open(outFile)
    outputAnswer = output.readline()
    # assert
    output.close()
    inputAnswer.close()
    self.assertEqual(result, outputAnswer)
     
if __name__ == '__main__':
  unittest.main()