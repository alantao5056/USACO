"""
ID: alantao2
LANG: PYTHON3
PROG: numtri
"""
currentListIndex = 0
lastListIndex = 0
count = 0
maxCount = 0

numtriInput = open('numtri_test_6.in', 'r')
numtriOutput = open('numtri.out', 'w')
length = int(numtriInput.readline().strip())
triangle = []

triangle.append([])
for i in range(0, length):
  line = numtriInput.readline().strip().split()
  triangle.append(list(map(int, line)))

numtriInput.close()

def largestSum(triangle: list, n: int) -> int:
  yPosition = [0] * (n + 1)
  x = 1
  visitied = [None] * (n + 1)
  maxSum = 0
  sums = [0] * (n + 1)
  while x > 0:
    y = yPosition[x]
    print(f"{x}  {y}")
    sums[x] = sums[x - 1] + triangle[x][y]
    if x != n:
      if visitied[x] == None:
        visitied[x] = 'left'
        x += 1
        yPosition[x] = y
      elif visitied[x] == 'left':
        visitied[x] = 'right'
        x += 1
        yPosition[x] = y + 1
      else:
        visitied[x] = None
        x -= 1
    else:
      if sums[x] > maxSum:
        maxSum = sums[x]
      x -= 1
  return maxSum

numtriOutput.write(str(largestSum(triangle, length)) + '\n')