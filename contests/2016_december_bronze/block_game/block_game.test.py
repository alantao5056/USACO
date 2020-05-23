import unittest
from block_game import block_game

class block_gameTest(unittest.TestCase):
  def test_1(self):
    cards = [['fox', 'box'], ['dog', 'cat'], ['car', 'bus']]
    alphabet = block_game(cards)
    self.assertEqual(alphabet, [2, 2, 2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0])

if __name__ == '__main__':
  unittest.main()