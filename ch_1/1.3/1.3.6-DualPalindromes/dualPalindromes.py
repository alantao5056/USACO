"""
ID: alantao2
LANG: PYTHON3
PROG: dualpal
"""

import math

def base10toBase(num: int, base: int) -> int:
  string = ''
  while num >= base:
    remainder = num % base
    string = str(remainder) + string
    num = math.floor(num / base)
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

dualpalInput = open('dualpal.in', 'r')
dualpalOutput = open('dualpal.out', 'w')

line = dualpalInput.readline().strip().split()
quantity = int(line[0])
num = int(line[1])

num += 1
count = 0 
oneWrite = False
while count != quantity:
  for i in range(2, 11):
    baseN = base10toBase(num, i)
    if ifPalindromic(baseN):
      if oneWrite == True:
        dualpalOutput.write(str(num) + '\n')
        count += 1
        break
      else:
        oneWrite = True
  num += 1
  oneWrite = False