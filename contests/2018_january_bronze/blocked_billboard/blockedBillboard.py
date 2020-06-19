def main(inputFile, outputFile):
  billboardInput = open(inputFile, 'r')
  billboardOutput = open(outputFile, 'w')
  lawnmower = billboardInput.readline().strip().split()
  cowFeed = billboardInput.readline().strip().split()
  for i in range(0, 4):
    lawnmower[i] = int(lawnmower[i])
    cowFeed[i] = int(cowFeed[i])
  billboardInput.close()
  billboardOutput.write(str(getSmallestRect(lawnmower, cowFeed)) + '\n')
  billboardOutput.close()

def isPointInRect(x, y, rectLowX, rectHighX, rectLowY, rectHighY):
  if x > rectLowX and x < rectHighX and y > rectLowY and y < rectHighY:
    return True
  return False

def getSmallestRect(lawnmower, cowFeed):
  rectLowX = 1001
  rectHighX = -1001
  for num in range(0, len(cowFeed), 2):
    x = cowFeed[num]
    if x < rectLowX:
      rectLowX = x
    if x > rectHighX:
      rectHighX = x
  
  rectLowY = 1001
  rectHighY = -1001
  for num in range(1, len(cowFeed), 2):
    y = cowFeed[num]
    if y < rectLowY:
      rectLowY = y
    if y > rectHighY:
      rectHighY = y
  
  lawnmowerLowX = 1001
  lawnmowerLowY = 1001
  lawnmowerHighX = -1001
  lawnmowerHighY = -1001 
  for i in range(lawnmower[0], lawnmower[2] + 1):
    for j in range(lawnmower[1], lawnmower[3] + 1):
      if isPointInRect(i, j, rectLowX, rectHighX, rectLowY, rectHighY) == False:
        if i < lawnmowerLowX:
          lawnmowerLowX = i
        elif i > lawnmowerHighX:
          lawnmowerHighX = i
        if j < lawnmowerLowY:
          lawnmowerLowY = j
        elif j > lawnmowerHighY:
          lawnmowerHighY = j
  return (lawnmowerHighX - lawnmowerLowX) * (lawnmowerHighY - lawnmowerLowY)
      

main('billboard.in', 'billboard.out')