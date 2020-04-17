"""
ID: alantao2
LANG: PYTHON3
PROG: pprime
"""

import math

def isPrime(n: int) -> bool:
  if n == 2:
    return True
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def toString(num: int, target: int) -> str:
  numStr = str(num)
  if target <= len(numStr):
    return numStr
  else:
    num = str(num)
    num = list(num)
    for i in range(0, target - len(numStr)):
      num.insert(0, 0)
    strings = [str(integer) for integer in num]
    a_string = "".join(strings)
    return a_string

def getCombination(start: int, end: int) -> list:
  hash = set()
  if start <= 2:
    hash.add(2)
    yield 2

  for i in range(1, len(str(end)) + 1):
    if i == 1:
      for j in range(3, 10):
        if j % 2 != 0 and j <= end and j >= start and j not in hash:
          hash.add(j)
          yield j
    else:
      integers = [1]
      halfLen = math.floor(i / 2)
      for j in range(0, halfLen - 1):
        integers.append(0)
      strings = [str(integer) for integer in integers]
      a_string = "".join(strings)
      integers = int(a_string)

      if i % 2 != 0:
        for k in range(1, integers * 10, 2):
          k = toString(k, halfLen)
          for num in range(0, 10):
            pal = f'{str(k)[::-1]}{num}{k}'
            if pal[0] != '0':
              pal = int(pal)
              if pal <= end and pal >= start and pal not in hash:
                hash.add(pal)
                yield pal
      else:
        for k in range(1, integers * 10, 2):
          k = toString(k, halfLen)
          pal = f'{str(k)[::-1]}{k}'
          if pal[0] != '0':
            pal = int(pal)
            if pal <= end and pal >= start and pal not in hash:
              hash.add(pal)
              yield pal

pprimeInput = open('pprime.in', 'r')
pprimeOutput = open('pprime.out', 'w')
line = pprimeInput.readline().strip().split()
pprimeInput.close()

result = []
for n in getCombination(int(line[0]), int(line[1])):
  if isPrime(n):
    result.append(n)
    
result = sorted(result)

for item in result:
  pprimeOutput.write(str(item) + '\n')
pprimeOutput.close()