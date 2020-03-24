import math

def ifPalindromic(num: int) -> bool:
  numStr = str(num)
  length = math.floor(len(numStr) / 2)
  j = len(numStr) - 1
  for i in range(0, math.floor(length)):
    if numStr[j] != numStr[i]:
      return False
    j -= 1
  return True

print(ifPalindromic(19911))