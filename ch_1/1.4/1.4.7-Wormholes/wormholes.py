"""
ID: alantao2
LANG: PYTHON3
PROG: wormhole
"""

wormholeInput = open('wormhole.in', 'r')
wormholeOutput = open('wormhole.out', 'w')

N = int(wormholeInput.readline().strip())
X = [0] * (N + 1)
Y = [0] * (N + 1)
nextOnRight = [0] * (N + 1)
partner = [0] * (N + 1)

def findNextOnRight():
  for i in range(1, N + 1):
    # next on right
    for j in range(1, N + 1):
      if X[j] > X[i] and Y[i] == Y[j]: # j right of i
        if nextOnRight[i] == 0 or X[j] < X[nextOnRight[i]]:
          nextOnRight[i] = j

def readInput():
  for i in range(1, N + 1):
    line = wormholeInput.readline().strip().split()
    X[i] = int(line[0])
    Y[i] = int(line[1])

def isCycle():
  for start in range(1, N + 1):
    pos = start
    for count in range(0, N):
      pos = nextOnRight[partner[pos]]
    if pos != 0:
      return True
  return False

def solve(start):
  total = 0
  i = start
  while i <= N:
    if partner[i] == 0:
      break
    i += 1
  
  if i > N:
    if isCycle():
      return 1
    else:
      return 0
  
  for j in range(i + 1, N + 1):
    if partner[j] == 0:
      partner[i] = j
      partner[j] = i
      total += solve(i + 1)
      partner[i] = 0
      partner[j] = 0

  return total

readInput()
findNextOnRight()
wormholeOutput.write(str(solve(1)) + '\n')