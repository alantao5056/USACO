def main(inputFile, outputFile):
  teleportInput = open(inputFile, 'r')
  teleportOutput = open(outputFile, 'w')
  
  line = teleportInput.readline().strip().split()
  line = list(map(int, line))
  a, b, x, y = line
  
  teleportInput.close()
  
  teleportOutput.write(str(getMinStep(a, b, x, y)) + '\n')
  
  teleportOutput.close()
  
def getMinStep(a, b, x, y):
  noTeleport = max(a, b) - min(a, b)
  nearestTeleporter, distance = getNearestTeleporter(a, x, y)
  
  if nearestTeleporter == x:
    teleportDistance = distance + getDistance(y, b)
  else:
    teleportDistance = distance + getDistance(x, b)
  
  return min(noTeleport, teleportDistance)
  
def getNearestTeleporter(a, x, y):
  teleportX = getDistance(a, x)
  teleportY = getDistance(a, y)
  nearestTeleporter = min(teleportX, teleportY)
  if nearestTeleporter == teleportX:
    return (x, teleportX)
  else:
    return (y, teleportY)

def getDistance(a, b):
  return max(a, b) - min(a, b)

main('teleport.in', 'teleport.out')