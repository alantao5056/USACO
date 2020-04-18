"""
ID: alantao2
LANG: PYTHON3
PROG: sprime
"""

import math

def primeNumbers(num: int) -> list:
  array = [True] * (num + 1)
  array[0] = False
  array[1] = False
  for j in range(0, math.floor(math.sqrt(num)) + 1):
    if array[j]:
      for k in range(j + j, num + 1, j):
        array[k] = False
  return array


def getCombination(length: int) -> list:
  start = '1'
  for i in range(length - 1):
    start += '0'
  start = int(start)
  primeHash = primeNumbers(start * 10 - 1)
  for j in range(start, start * 10):
    if primeHash[j]:
      num = j
      for k in range(length - 1):
        num = math.floor(num / 10)
        if primeHash[num] == False:
          break
      else:
        yield j

sprimeInput = open('sprime.in', 'r')
sprimeOutput = open('sprime.out', 'w')

length = int(sprimeInput.readline().strip())
sprimeInput.close()
for num in getCombination(length):
  sprimeOutput.write(str(num) + '\n')