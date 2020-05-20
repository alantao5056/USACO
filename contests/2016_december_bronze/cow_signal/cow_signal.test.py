import unittest
from cow_signal import amplifySignal

class amplifySignalTest(unittest.TestCase):
  def test_1(self):
    signal = [
      ['X', 'X', 'X', '.'],
      ['X', '.', '.', 'X'],
      ['X', 'X', 'X', '.'],
      ['X', '.', '.', 'X'],
      ['X', 'X', 'X', '.']
    ]

    amplifiedSignal = amplifySignal(signal)

    self.assertEqual(amplifiedSignal[0], list("XXXXXX.."))
    self.assertEqual(amplifiedSignal[1], list("XXXXXX.."))
    self.assertEqual(amplifiedSignal[2], list("XX....XX"))
    self.assertEqual(amplifiedSignal[3], list("XX....XX"))
    self.assertEqual(amplifiedSignal[4], list("XXXXXX.."))
    self.assertEqual(amplifiedSignal[5], list("XXXXXX.."))
    self.assertEqual(amplifiedSignal[6], list("XX....XX"))
    self.assertEqual(amplifiedSignal[7], list("XX....XX"))
    self.assertEqual(amplifiedSignal[8], list("XXXXXX.."))
    self.assertEqual(amplifiedSignal[9], list("XXXXXX.."))

if __name__ == '__main__':
  unittest.main()