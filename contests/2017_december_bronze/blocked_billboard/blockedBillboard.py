def main(inputFile, outputFile):
  billboardInput = open(inputFile, 'r')
  billboardOutput = open(outputFile, 'w')
  board1Line = billboardInput.readline().strip().split()
  board1 = [int(board1Line[0]), int(board1Line[1]), int(board1Line[2]), int(board1Line[3])]
  board2Line = billboardInput.readline().strip().split()
  board2 = [int(board2Line[0]), int(board2Line[1]), int(board2Line[2]), int(board2Line[3])]
  truckLine = billboardInput.readline().strip().split()
  truck = [int(truckLine[0]), int(truckLine[1]), int(truckLine[2]), int(truckLine[3])]
  billboardInput.close()
  billboardOutput.write(str(getNotBlocked(board1, board2, truck)) + '\n')
  billboardOutput.close()

def getArea(x1, y1, x2, y2):
  if x1 > x2:
    length = x1 - x2
  else:
    length = x2 - x1
  if y1 > y2:
    width = y1 - y2
  else:
    width = y2 - y1
  return length * width

# print(getArea(6, 0, 10, 4))

def projection(x1, x2, x3, x4):
  if x1 < x2 <= x3 < x4:
    return 0
  if x3 < x4 <= x1 < x2:
    return 0
  if x1 < x3 < x2 < x4:
    return x2 - x3
  if x1 < x3 < x4 < x2:
    return x4 - x3
  if x3 < x1 < x2 < x4:
    return x2 - x1
  if x3 < x1 < x4 < x2:
    return x4 - x1

def getNotBlocked(board1: list, board2: list, truck: list):
  boardsArea = getArea(board1[0], board1[1], board1[2], board1[3]) + getArea(board2[0], board2[1], board2[2], board2[3])
  # print(boardsArea)
  
  board1X = projection(board1[0], board1[2], truck[0], truck[2])
  board1Y = projection(board1[1], board1[3], truck[1], truck[3])
  
  board2X = projection(board2[0], board2[2], truck[0], truck[2])
  board2Y = projection(board2[1], board2[3], truck[1], truck[3])
  
  board1Area = board1X * board1Y
  board2Area = board2X * board2Y
  
  return boardsArea - board1Area - board2Area
  
main('billboard.in', 'billboard.out')