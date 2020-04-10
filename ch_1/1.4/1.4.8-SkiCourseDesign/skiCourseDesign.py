"""
ID: alantao2
LANG: PYTHON3
PROG: skidesign
"""

import math

skidesignInput = open('skidesign.in', 'r')
skidesignOutput = open('skidesign.out', 'w')

hills = [0] * 101
smallest = math.inf
biggest = 0
minCost = math.inf
hillsNum = int(skidesignInput.readline().strip())
L = 18

for i in range(0, hillsNum):
  h = int(skidesignInput.readline().strip())
  if h < smallest:
    smallest = h
  elif h > biggest:
    biggest = h
  hills[h] += 1

for start in range(smallest, biggest - L + 2):
  end = start + L -1
  cost = 0
  for left in range(smallest, start):
    if hills[left] != 0:
      cost += (start - left) ** 2 * hills[left]
  for right in range(end + 1, biggest + 1):
    if hills[right] != 0:
      cost += (right - end) ** 2 * hills[right]
  if cost < minCost:
    minCost = cost
  print(str(start) + '-' + str(end))
skidesignOutput.write(str(minCost) + '\n')