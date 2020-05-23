def getSmallBig(array: list):
  smallest = 11
  biggest = -1
  for num in array:
    if num < smallest:
      smallest = num
    elif num > biggest:
      biggest = num
  return [smallest, biggest]

def getLength(x: list, y: list):
  smallBigX = getSmallBig(x)
  smallBigY = getSmallBig(y)
  xLen = smallBigX[1] - smallBigX[0]
  yLen = smallBigY[1] - smallBigY[0]
  if xLen > yLen:
    return xLen ** 2
  return yLen ** 2

def main(inputFile, outputFile):
  squareInput = open(inputFile, 'r')
  square_1 = squareInput.readline().strip().split()
  square_2 = squareInput.readline().strip().split()
  x = [int(square_1[0]), int(square_1[2]), int(square_2[0]), int(square_2[2])]
  y = [int(square_1[1]), int(square_1[3]), int(square_2[1]), int(square_2[3])]
  squareInput.close()
  squareOutput = open(outputFile, 'w')
  squareOutput.write(str(getLength(x, y)) + '\n')
  squareOutput.close()
  
main('square.in', 'square.out')