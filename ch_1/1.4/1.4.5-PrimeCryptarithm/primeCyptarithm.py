"""
ID: alantao2
LANG: PYTHON3
PROG: crypt1
"""

import math

def validConbination(array: list) -> bool:
  a = array[0]
  b = array[1]
  tensPlaceCheck = str(a * int(str(b)[0]))
  onesPlaceCheck = str(a * (b - 10 * (int(str(b)[0]))))
  if len(tensPlaceCheck) != 3 or len(onesPlaceCheck) != 3:
    return False
  abCheck = str(a * b)
  for num in tensPlaceCheck:
    if int(num) not in numsSet:
      return False
  for num in onesPlaceCheck:
    if int(num) not in numsSet:
      return False
  for num in abCheck:
    if int(num) not in numsSet:
      return False
  return True

crypt1Input = open('crypt1.in', 'r')
crypt1Output = open('crypt1.out', 'w')

numAmount = int(crypt1Input.readline().strip())
numsArray = crypt1Input.readline().strip().split()
numsSet = set()
count = 0

for p in range(0, len(numsArray)):
  numsSet.add(int(numsArray[p]))
possibleX = []
possibleY = []

for i in range(0, len(numsArray)):
  for j in range(0, len(numsArray)):
    for k in range(0, len(numsArray)):
      number = int(numsArray[i]) * 100 + int(numsArray[j]) * 10 + int(numsArray[k])
      possibleX.append(number)
      if i == 0:
        possibleY.append(int(numsArray[j]) * 10 + int(numsArray[k]))

conbination = []
for x in range(0, len(possibleX)):
  for y in range(0, len(possibleY)):
    conbination.append([possibleX[x], possibleY[y]])

for com in conbination:
  if validConbination(com):
    count += 1
crypt1Output.write(str(count) + '\n')