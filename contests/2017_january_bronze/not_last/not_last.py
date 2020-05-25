import math

def main(inputFile, outputFile):
  notLastInput = open(inputFile, 'r')
  notLastOutput = open(outputFile, 'w')
  entries = int(notLastInput.readline().strip())
  chart = {}
  for _ in range(0, entries):
    name, num = notLastInput.readline().strip().split()
    if name not in chart:
      chart[name] = int(num)
    else:
      chart[name] += int(num)
  notLastInput.close()
  notLastOutput.write(getSecondSmall(chart) + '\n')
  notLastOutput.close()

def findSmallest(chart: list):
  smallest = 10000000
  for name in chart.keys():
    if chart[name] < smallest:
      smallest = chart[name]
  return smallest

def getSecondSmall(chart: list):
  if len(chart) == 1:
    keys = chart.keys()
    for name in keys:
      return name
  smallestName = ''
  smallest = findSmallest(chart)
  chart = {key:val for key, val in chart.items() if val != smallest}
  if not chart:
    return 'Tie'
  secondSmallest = findSmallest(chart)
  for name in chart.keys():
    if chart[name] == secondSmallest:
      if smallestName == '':
        smallestName = name
      else:
        return 'Tie'
  return smallestName
  
  
main('notlast.in', 'notlast.out')