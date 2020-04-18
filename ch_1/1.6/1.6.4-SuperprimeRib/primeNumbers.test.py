import unittest
from superprimeRib import primeNumbers

class generatePrimeNumsTest(unittest.TestCase):
  def test_1(self):
    result = primeNumbers(10)

    primes = []
    for i in range(0, len(result)):
      if result[i]:
        primes.append(i)

    self.assertEqual(primes, [2, 3, 5, 7])

  # def test_2(self):
  #   result = groupByDigits(100)
  #   self.assertEqual(result, [[2, 3, 5, 7], [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]])

if __name__ == '__main__':
  unittest.main()