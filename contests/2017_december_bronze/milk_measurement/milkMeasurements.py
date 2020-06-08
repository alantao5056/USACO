def main(inputFile, outputFile):
  measurementInput = open(inputFile, 'r')
  measurementOutput = open(outputFile, 'w')
  N = int(measurementInput.readline().strip())
  log = []
  for _ in range(0, N):
    line = measurementInput.readline().strip().split()
    log.append([int(line[0]), line[1], line[2]])
  measurementInput.close()
  measurementOutput.write(str(getChangeDisplay(log)) + '\n')
  measurementOutput.close()
  
def getGreatestMilk(milkHash):
  greatest = 0
  for item in milkHash.keys():
    if milkHash[item] > greatest:
      greatest = milkHash[item]
  return [k for k,v in milkHash.items() if v == greatest]
  
def getChangeDisplay(log: list):
  # sort by days
  log.sort()
  # create hash
  milkHash = {
    'Bessie': 7,
    'Elsie': 7,
    'Mildred': 7,
  }
  greatestName = []
  count = 0
  # cycle
  for line in log:
    name = line[1]
    value = line[2]
    milkHash[name] += int(value)
    milkNames = getGreatestMilk(milkHash)
    if greatestName != milkNames:
      greatestName = milkNames
      count += 1
  return count

main('measurement.in', 'measurement.out')