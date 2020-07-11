def main(inputFile, outputFile):
  pailsInput = open(inputFile, 'r')
  pailsOutput = open(outputFile, 'w')
  
  X, Y, M = pailsInput.readline().split()
  X, Y, M = int(X), int(Y), int(M)
  pailsInput.close()
  pailsOutput.write(str(getMostFillOfM(X, Y, M)) + '\n')
  pailsOutput.close()
  
def getMostFillOfM(X, Y, M) -> int:
  mostFillX = getMostFill(X, M)
  mostFillY = getMostFill(Y, M)
  mostFill = -1
  
  for i in range(0, mostFillX + 1):
    for j in range(0, mostFillY + 1):
      fill = i * X + j * Y
      if fill <= M:
        mostFill = max(mostFill, fill)
  return mostFill

def getMostFill(X, target):
  count = 0
  curFill = 0
  
  while curFill < target:
    curFill += X
    count += 1
  return count

main('pails.in', 'pails.out')