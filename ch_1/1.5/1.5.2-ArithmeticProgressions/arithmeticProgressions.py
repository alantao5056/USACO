"""
ID: alantao2
LANG: PYTHON3
PROG: ariprog
"""

ariprogInput = open('ariprog.in', 'r')
ariprogOutput = open('ariprog.out', 'w')

length = int(ariprogInput.readline().strip())
bisquares = int(ariprogInput.readline().strip())
bisquaresComb = []
comb = set()

def ifValidAriprog(a: int, b: int) -> bool:
  for i in range(0, length):
    if a + i * b not in comb:
      return False
  return True

for i in range(0, bisquares + 1):
  bisquaresComb.append(i)

for q in range(0, len(bisquaresComb)):
  for p in range(q, len(bisquaresComb)):
    comb.add(q ** 2 + p ** 2)

none = True
for i in range(1, 12000):
  for j in range(0, 12000):
    if ifValidAriprog(j, i):
      none = False
      ariprogOutput.write(str(j) + ' ' + str(i) + '\n')
if none:
  ariprogOutput.write('NONE\n')