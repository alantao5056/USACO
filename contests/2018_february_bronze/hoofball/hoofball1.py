from itertools import chain
import collections

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
  getBallHash = set()
  covered = set()
  count = 0
  for position in positions:
    positionCover = getPositionCover(positions, position)
    getBallHash.add(positionCover)

  target = set()
  while covered != set(positions):
    count += 1
    maxCover = getMaxCover(getBallHash, target)
    getBallHash.remove(maxCover)
    covered |= set(maxCover)
    target = covered
  
  return count
  
def getMaxCover(ballHash: set, target):
  ballHash = list(ballHash)
  bigOverlapCount = -1
  bigCover = set()
  if len(target) == 0:
    biggestLength = 0
    biggest = set()
    for b in ballHash:
      if len(b) > biggestLength:
        biggest = b
        biggestLength = len(b)
    return biggest
  
  for cover in ballHash:
    notOverlapCount = 0
    for c in cover:
      if c not in target:
        notOverlapCount += 1
    if notOverlapCount > bigOverlapCount:
      bigOverlapCount = notOverlapCount
      bigCover = cover
  return tuple(bigCover)
    
def getPositionCover(positions, position):
  ballHash = set()
  ballHash.add(position)
  loop = True
  
  curCow = position
  while loop:
    smallest = 10000
    smallestIndex = 0
    for p in range(0, len(positions)):
      if positions[p] != curCow:
        distance = getDistance(positions[p], curCow)
        if distance < smallest:
          smallest = distance
          smallestIndex = p
    if positions[smallestIndex] in ballHash:
      return tuple(ballHash)
    ballHash.add(positions[smallestIndex])
    curCow = positions[smallestIndex]
  return tuple(ballHash)

def getDistance(a, b):
  return max(a, b) - min(a, b)

main('hoofball.in', 'hoofball.out')