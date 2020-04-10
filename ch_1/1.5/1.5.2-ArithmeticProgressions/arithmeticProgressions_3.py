"""
ID: alantao2
LANG: PYTHON3
PROG: ariprog
"""

ariprogInput = open('ariprog.in', 'r')
ariprogOutput = open('ariprog.out', 'w')

N = int(ariprogInput.readline().strip())
M = int(ariprogInput.readline().strip())

class Result:
  def __init__(self, a, b):
    self.a = a
    self.b = b

squares = []
for i in range(0, M + 1):
  squares.append(i ** 2)

hashNums = [False] * (M * M * 2 + 1)
nums = [] * (M * M * 2 + 1) 

for j in range(0, M + 1):
  for k in range(j, M + 1):
    sum = squares[j] + squares[k]
    if not hashNums[sum]:
      hashNums[sum] = True
      nums.append(sum)

nums = sorted(nums)
numsLength = len(nums)
max = nums[-1]

results = []
for i in range(0, numsLength):
  a = nums[i]
  for j in range(i + 1, numsLength):
    b = nums[j] - nums[i]

    n = a + b * (N - 1)
    if n > max:
      break

    k = 2
    while k < N:
      if not hashNums[n]:
        break
      n -= b
      k += 1

    if k == N:
      results.append(Result(a, b))

results = sorted(results, key=lambda r: (r.b, r.a))

if len(results) == 0:
  ariprogOutput.write('NONE\n')
else:
  for r in results:
    ariprogOutput.write(str(r.a) + ' ' + str(r.b) + '\n')