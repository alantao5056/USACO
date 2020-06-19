def main(inputFile, outputFile):
  lifeguardsInput = open(inputFile, 'r')
  lifeguardsOutput = open(outputFile, 'w')
  N = int(lifeguardsInput.readline().strip())
  lifeguards = []
  for _ in range(0, N):
    line = lifeguardsInput.readline().strip().split()
    lifeguards.append([int(line[0]), int(line[1])])
  lifeguards.sort()
  # print(getTime(lifeguards))
  lifeguardsInput.close()
  lifeguardsOutput.write(str(getMaxTimeWhenFired(lifeguards)) + '\n')
  lifeguardsOutput.close()
  
def deepCopy(array: list) -> list:
  newArray = []
  for item in array:
    newArray.append([item[0], item[1]])
  return newArray

def getTime(array: list) -> int:
  copy = deepCopy(array)
  time = 0
  i = 0
  while i < len(copy) - 1:
    if copy[i][1] > copy[i + 1][0] and copy[i][1] < copy[i + 1][1]:
      copy[i][1] = copy[i + 1][0]
    elif copy[i][1] > copy[i + 1][0] and copy[i][1] > copy[i + 1][1]:
      copy.remove(copy[i + 1])
      continue
    i += 1
  
  for cow in copy:
    time += cow[1] - cow[0]
  return time

def getMaxTimeWhenFired(lifeguards):
  maxTime = -1
  for cow in lifeguards:
    newList = [x for x in lifeguards if x != cow]
    curTime = getTime(newList)
    if curTime > maxTime:
      maxTime = curTime
  return maxTime

main('lifeguards.in', 'lifeguards.out')