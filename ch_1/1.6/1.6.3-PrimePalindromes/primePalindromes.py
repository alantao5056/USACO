"""
ID: alantao2
LANG: PYTHON3
PROG: pprime
"""

import math

def isPrime(n) -> bool:
  if n == 2:
    return True
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def generatePalindromes(start: int, end: int) -> list:
  p = []
  for i in range(start, end + 1):
    stringI = str(i)
    stringLength = len(stringI)
    k = 0
    j = stringLength - 1
    flag = True
    while j >= 0 and k < stringLength and j < stringLength:
      if stringI[j] != stringI[k]:
        flag = False
        break
      j -= 1
      k += 1
    if flag and isPrime(i):
      p.append(i)
  return p

pprimeInput = open('pprime.in', 'r')
pprimeOutput = open('pprime.out', 'w')
line = pprimeInput.readline().strip().split()
pprimeInput.close()

palindromes = generatePalindromes(int(line[0]), int(line[1]))

for item in palindromes:
  pprimeOutput.write(str(item) + '\n')
pprimeOutput.close()