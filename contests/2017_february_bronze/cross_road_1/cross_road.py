def main(inputFile, outputFile):
  crossRoadInput = open(inputFile, 'r')
  crossRoadOutput = open(outputFile, 'w')
  N = int(crossRoadInput.readline().strip())
  data = []
  for _ in range(0, N):
    data.append(crossRoadInput.readline().strip().split())
  crossRoadInput.close()
  crossRoadOutput.write(str(getNumOfCross(data)) + '\n')
  crossRoadOutput.close()
  
def getNumOfCross(data: list):
  crossCount = 0
  crossHash = ['-1'] * 10
  for record in data:
    if crossHash[int(record[0]) - 1] == '-1':
      crossHash[int(record[0]) - 1] = record[1]
    elif crossHash[int(record[0]) - 1] != record[1]:
      crossCount += 1
      crossHash[int(record[0]) - 1] = record[1]
  return crossCount
  
main('crossroad.in', 'crossroad.out')