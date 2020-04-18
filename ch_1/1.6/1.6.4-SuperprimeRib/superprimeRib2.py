"""
ID: alantao2
LANG: PYTHON3
PROG: sprime
"""

import math
# from timeit import default_timer as timer

def isPrime(n: int) -> bool:
  if n == 2:
    return True
  for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

sprimeInput = open('sprime.in', 'r')
sprimeOutput = open('sprime.out', 'w')

length = int(sprimeInput.readline().strip())
sprimeInput.close()

def tryAllPossible(n: int) -> list:
  prime = [1, 3, 7, 9]
  if length == 1:
    sprimeOutput.write(f'{n}\n')
  else:
    for num in prime:
      integer = n * 10 + num
      if isPrime(integer):
        if len(str(integer)) == length:
          sprimeOutput.write(f'{integer}\n')
        else:
          tryAllPossible(integer)
    return
# start = timer()
for n in [2, 3, 5, 7]:
  tryAllPossible(n)
sprimeOutput.close()
# end = timer()
# print(end - start)
# print(isPrime(9))