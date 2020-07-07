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
  cows = sorted(cows)
  mostBuckets = 0
  for i in range(1, 1000):
    curBuckets = 0
    for cow in cows:
      if cow[0] <= i <= cow[1]:
        curBuckets += cow[2]
    if curBuckets > mostBuckets:
      mostBuckets = curBuckets
  return mostBuckets
        
main('blist.in', 'blist.out')