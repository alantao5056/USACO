def main(inputFile, outputFile):
  cowqueueInput = open(inputFile, 'r')
  cowqueueOutput = open(outputFile, 'w')
  N = int(cowqueueInput.readline().strip())
  cows = []
  for _ in range(0, N):
    line = cowqueueInput.readline().strip().split()
    cows.append([int(line[0]), int(line[1])])
  cowqueueInput.close()
  cows.sort()
  cowqueueOutput.write(str(getTime(cows)) + '\n')
  cowqueueOutput.close()

def getTime(cows: list):
  curTime = cows[0][0] + cows[0][1]
  for cow in range(1, len(cows)):
    if curTime <= cows[cow][0]:
      curTime = cows[cow][0] + cows[cow][1]
    else:
      curTime += cows[cow][1]
  return curTime

main('cowqueue.in', 'cowqueue.out')