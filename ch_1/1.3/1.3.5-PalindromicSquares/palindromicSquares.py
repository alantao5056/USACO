"""
ID: alantao2
LANG: PYTHON3
PROG: palsquare
"""

palsquareInput = open('palsquare.in', 'r')
palsquareOutput = open('palsquare.out', 'w')
base = int(palsquareInput.readline().strip())

import math

def base10toBase(num: int, base: int) -> int:
  numsToLetters = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K'
  }
  string = ''
  while num >= base:
    remainder = num % base
    if remainder > 9:
      string = numsToLetters[remainder] + string
    else:
      string = str(remainder) + string
    num = math.floor(num / base)
  if num > 9:
    string = numsToLetters[num] + string
    result = string
  else:
    result = str(num) + string
  return result

def ifPalindromic(num: int) -> bool:
  numStr = str(num)
  length = math.floor(len(numStr) / 2)
  j = len(numStr) - 1
  for i in range(0, math.floor(length)):
    if numStr[j] != numStr[i]:
      return False
    j -= 1
  return True

for i in range(1, 301):
  square = base10toBase(i ** 2, base)
  if ifPalindromic(square):
    numBase = base10toBase(i, base)
    palsquareOutput.write(numBase + ' ' + square + '\n')
