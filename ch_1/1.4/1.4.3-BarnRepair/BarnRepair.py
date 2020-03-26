"""
ID: alantao2
LANG: PYTHON3
PROG: barn1
"""

import math

def sort(array: list) -> list:
  less = []
  equal = []
  greater = []

  if len(array) > 1:
    pivot = array[0]
    for x in array:
      if x < pivot:
        less.append(x)
      elif x == pivot:
        equal.append(x)
      elif x > pivot:
        greater.append(x)
    return sort(less)+equal+sort(greater)
  else:
    return array

def biggestGaps(num: int, arr: list) -> list:
  count = 0
  biggest = 0
  for j in range(0, num):
    for i in range(0, len(arr)):
      if arr[i] > biggest:
        biggest = arr[i]
    arr.remove(biggest)
    count += biggest
    biggest = 0
  return count

barn1Input = open('barn1.in', 'r')
barn1Output = open('barn1.out', 'w')

firstLine = barn1Input.readline().strip().split()
maxBoard = int(firstLine[0])
stallsNum = int(firstLine[1])
cowsNum = int(firstLine[2])
stalls = []
gaps = []

for i in range(0, cowsNum):
  line = int(barn1Input.readline().strip())
  stalls.append(line)

stalls = sort(stalls)

for i in range(1, len(stalls)):
  gaps.append(stalls[i] - stalls[i - 1] - 1)
if maxBoard > cowsNum:
  barn1Output.write(str(cowsNum) + '\n')
else:
  barn1Output.write(str(stalls[-1] - stalls[0] + 1 - biggestGaps(maxBoard - 1, gaps)) + '\n')