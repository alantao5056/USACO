import unittest
from superprimeRib import getCombination

class getCombinationTest(unittest.TestCase):
  def test_1(self):
    result = getCombination(5)
    self.assertEqual(list(result), [23333,23339,23399,23993,29399,31193,31379,37337,37339,37397,59393,59399,71933,73331,73939])
if __name__ == '__main__':
  unittest.main()