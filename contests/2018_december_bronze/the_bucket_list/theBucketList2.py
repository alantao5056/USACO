def main(inputFile: str, outputFile: str):
  blistInput = open(inputFile, 'r')
  blistOutput = open(outputFile, 'w')
  
  N = int(blistInput.readline().strip())
  cows = []
  for _ in range(0, N):
    line = blistInput.readline().strip().split()
    line = list(map(int, line))
    cows.append(line)
  
  blistInput.close()
  
  blistOutput.write(str(getMinBuckets(cows)) + '\n')
  
  blistOutput.close()

def getMinBuckets(cows: list) -> int:
  timeLineHash = {}
  for i in range(1, 1001):
    timeLineHash[i] = 0
  
  for cow in cows:
    for j in range(cow[0], cow[1] + 1):
      timeLineHash[j] += cow[2]
  
  mostBuckets = 0
  for key in timeLineHash.keys():
    if timeLineHash[key] > mostBuckets:
      mostBuckets = timeLineHash[key]
  return mostBuckets