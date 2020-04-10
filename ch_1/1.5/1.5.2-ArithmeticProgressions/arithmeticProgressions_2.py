"""
ID: alantao2
LANG: PYTHON3
PROG: ariprog
"""

ariprogInput = open('ariprog.in', 'r')
ariprogOutput = open('ariprog.out', 'w')

length = int(ariprogInput.readline().strip())
M = int(ariprogInput.readline().strip())
allBisquares = []
squares = []
comb = set()

class Result:
  def __init__(self, a, b):
    self.a = a
    self.b = b

for i in range(0, M + 1):
  squares.append(i ** 2)

for j in range(0, M + 1):
  for k in range(j, M + 1):
    if squares[j] + squares[k] not in comb:
      comb.add(squares[j] + squares[k])
      allBisquares.append(squares[j] + squares[k])

allBisquares = sorted(allBisquares)
min = allBisquares[0]
max = allBisquares[-1]
x = (max - min) / (length - 1)
for i in range(0, len(allBisquares)):
  if (i > x):
    print (i)
    break
maxIndex = i

max = (M ** 2) * 2
results = []
for i in range(0, maxIndex):
  for j in range(i, maxIndex):
    if allBisquares[i] < allBisquares[j]:
      b = allBisquares[j] - allBisquares[i]
      a = allBisquares[i]
    else:
      b = allBisquares[i] - allBisquares[j]
      a = allBisquares[j]
    if b == 0:
      continue

    n = a + b * (length - 1)
    if n > max:
      break;

    found = True
    print(f'{i} {j}')
    for k in range(2, length):
      if n not in comb:
        found = False
        break
      n -= b

    if found:
      results.append(Result(a, b))

results = sorted(results, key=lambda r: (r.b, r.a))

if len(results) == 0:
  ariprogOutput.write('NONE\n')
else:
  for r in results:
    ariprogOutput.write(str(r.a) + ' ' + str(r.b) + '\n')