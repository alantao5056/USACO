def main(inputFile, outputFile):
  shuffleInput = open(inputFile, 'r')
  shuffleOutput = open(outputFile, 'w')
  N = int(shuffleInput.readline().strip())
  line = shuffleInput.readline().strip().split()
  gotoPosition = []
  for num in line:
    gotoPosition.append(int(num))
  IDList = shuffleInput.readline().strip().split()
  # print(N)
  # print(gotoPosition)
  # print(IDList)
  result = getFinalPosition(gotoPosition, IDList)
  shuffleInput.close()
  for ele in result:
    shuffleOutput.write(ele + '\n')
  shuffleOutput.close()

def unShuffle(gotoPosition: list, IDList: list):
  newList = [''] * len(gotoPosition)
  for i in range(0, len(gotoPosition)):
    newList[i] = IDList[gotoPosition[i] - 1]
  return newList

def getFinalPosition(gotoPosition, IDList):
  shuffle1 = unShuffle(gotoPosition, IDList)
  shuffle2 = unShuffle(gotoPosition, shuffle1)
  shuffle3 = unShuffle(gotoPosition, shuffle2)
  return shuffle3

main('shuffle.in', 'shuffle.out')