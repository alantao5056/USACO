def main(inputFile, outputFile):
  hoofballInput = open(inputFile, 'r')
  hoofballOutput = open(outputFile, 'w')
  
  hoofballInput.readline()
  positions = hoofballInput.readline().strip().split()
  positions = list(map(int, positions))
  
  hoofballInput.close()
  hoofballOutput.write(str(getLeastAmountBall(positions)) + '\n')
  hoofballOutput.close()
  
def getLeastAmountBall(positions: list) -> int:
  count = 0
  # get who to pass
  positions.sort()
  passTo = [-1] * len(positions)
  
  passTo[0] = 1
  passTo[len(positions) - 1] = len(positions) - 2
  
  for i in range(1, len(positions) - 1):
    if positions[i] - positions[i - 1] <= positions[i + 1] - positions[i]:
      passTo[i] = i - 1
    else:
      passTo[i] = i + 1
  
  # get alone ones
  alone = []
  setPassTo = set(passTo)
  
  for i in range(0, len(positions)):
    if i not in setPassTo:
      alone.append(i)
  
  value = [False] * len(positions)
  
  for a in alone:
    value = getPositionCover(positions, a, value, passTo)
    count += 1
  
  if all(value):
    return count
  else:
    falseCount = 0
    for b in value:
      if not b:
        falseCount += 1
    return count + int(falseCount / 2)
  
  return value
  
def getPositionCover(positions, position, value, passTo):
  ballHash = set([position])
  curCow = position
  while True:
    value[curCow] = True
    curCow = passTo[curCow]
    if curCow in ballHash:
      return value
    ballHash.add(curCow)

def getNotTrue(value):
  for i in range(0, len(value)):
    if not value[i]:
      return i

main('hoofball.in', 'hoofball.out')