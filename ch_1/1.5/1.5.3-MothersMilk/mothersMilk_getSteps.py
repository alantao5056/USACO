"""
ID: alantao2
LANG: PYTHON3
PROG: milk3
"""

def pour(_from, to, toV):
  if _from + to <= toV:
    return (0, _from + to)
  elif toV - to < _from:
    return (_from - (toV - to), toV)
  return (_from, to)

result = set()

def search(a, b, c, steps, count):
  steps[count] = f"{a} {b} {c}"

  if visited[a][b][c]:
    return
  visited[a][b][c] = True
  if a == 0:
    print("A B C")
    print(f"{aV} {bV} {cV}")
    print("=======")
    for i in range(0, count + 1):
      print(steps[i])
    print("-----------------------------------")
    result.add(c)

  # a -> b
  newA, newB = pour(a, b, bV)
  search(newA, newB, c, steps, count + 1)

  # a -> c
  newA, newC = pour(a, c, cV)
  search(newA, b, newC, steps, count + 1)

  # b -> a
  newB, newA = pour(b, a, aV)
  search(newA, newB, c, steps, count + 1)

  # b -> c
  newB, newC = pour(b, c, cV)
  search(a, newB, newC, steps, count + 1)

  # c -> a
  newC, newA = pour(c, a, aV)
  search(newA, b, newC, steps, count + 1)

  # c -> b
  newC, newB = pour(c, b, bV)
  search(a, newB, newC, steps, count + 1)

milk3Input = open('milk3.in', 'r')
milk3Output = open('milk3.out', 'w')

line = milk3Input.readline().split()
milk3Input.close()
aV = int(line[0])
bV = int(line[1])
cV = int(line[2])

visited = [[[False for x in range(cV + 1)] for x in range(bV + 1)] for x in range(aV + 1)]
# milk3Output.write(getComb(a, b, c))

search(0, 0, cV, [""] * 100, 0)
output = ''
result = sorted(list(result))
for ele in result:
  output += f'{ele} '
milk3Output.write(output[:-1] + '\n')
milk3Output.close()