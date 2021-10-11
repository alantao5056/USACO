"""
ID: alantao
LANG: PYTHON3
TASK: prefix
"""

letterHash = {}
string = ""
maxIndex = 0

def solve(index: int, level):
  global string, maxIndex
  cur = string[index]
  avaliable = True
  if cur in level:
    if not solve(index + 1, level[cur]):
      avaliable = False
    
  if None in level:
    temp = solve(index, letterHash)
    if not avaliable:
      avaliable = temp
  
  if cur not in level and None not in level:
    return False

  if avaliable:
    maxIndex = max(maxIndex, index)
  return avaliable


def main(inputFile: str, outputFile: str):
  global string
  prefixInput = open(inputFile, 'r')
  prefixOutput = open(outputFile, 'w')

  arr = []
  cur = prefixInput.readline().strip().split()

  while cur != ["."]:
    arr += cur
    cur = prefixInput.readline().strip().split()
  
  for a in arr:
    # add a to letterHash
    level = letterHash
    for char in a:
      if char in level:
        level = level[char]
      else:
        level[char] = {}
        level = level[char]
    level[None] = {}

  # print(letterHash)
  cur = prefixInput.readline().strip()

  while len(cur) != 0:
    string += cur
    cur = prefixInput.readline().strip()

  string += '0'

  prefixInput.close()

  solve(0, letterHash)

  prefixOutput.write(str(maxIndex))
  prefixOutput.write("\n")

  prefixOutput.close()


main("prefix.in", "prefix.out")