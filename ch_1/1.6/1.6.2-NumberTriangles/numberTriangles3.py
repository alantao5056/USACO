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
  triangle.append(list(map(int, line)))

numtriInput.close()


def getLargestSum(triangle: list):
  for j in range(len(triangle) - 2, -1, -1):
    for num in range(0, len(triangle[j])):
      l = triangle[j + 1][num]
      r = triangle[j + 1][num + 1]
      if l > r:
        triangle[j][num] += l
      else:
        triangle[j][num] += r
  return triangle[0][0]

numtriOutput.write(str(getLargestSum(triangle)) + '\n')