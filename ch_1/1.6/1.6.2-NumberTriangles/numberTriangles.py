"""
ID: alantao2
LANG: PYTHON3
PROG: numtri
"""
currentListIndex = 0
lastListIndex = 0
count = 0
maxCount = 0

numtriInput = open('numtri.in', 'r')
numtriOutput = open('numtri.out', 'w')
length = int(numtriInput.readline().strip())
triangle = []

for i in range(0, length):
  line = numtriInput.readline().strip().split()
  for string in line:
    
    triangle.append(line)

numtriInput.close()
numsHash = {}

def getMax(x: int, y: int) -> int:
  if x == len(triangle) - 1:
    return int(triangle[x][y])
  if (x + 1, y) in numsHash:
    l = numsHash[(x + 1, y)]
  else:
    l = getMax(x + 1, y)
    numsHash[(x + 1, y)] = l
  if (x + 1, y + 1) in numsHash:
    r = numsHash[(x + 1, y + 1)]
  else:
    r = getMax(x + 1, y + 1)
    numsHash[(x + 1, y + 1)] = r
    
  if l >= r:
    return int(triangle[x][y]) + l
  else:
    return int(triangle[x][y]) + r

numtriOutput.write(str(getMax(0, 0)) + '\n')