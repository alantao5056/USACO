"""
ID: alantao2
LANG: PYTHON3
PROG: milk2
"""

class Farmer:
  def __init__(self, start, end):
    self.start = start
    self.end = end

milk2Input = open('milk2.in', 'r')
milk2Output = open('milk2.out', 'w')
farmers = []
farmersNum = int(milk2Input.readline().strip())

for i in range(0, farmersNum):
  farmer = milk2Input.readline().strip().split()
  start = int(farmer[0])
  end = int(farmer[1])
  farmers.append(Farmer(start, end))
farmers.sort(key = lambda f: f.start, reverse = False)
print(farmers)

maxMilkPeriod = farmers[0].end - farmers[0].start
maxNoMilkPeriod = 0
startConnection = farmers[0].start
endConnection = farmers[0].end

for i in range(1, len(farmers)):
  if farmers[i].start <= endConnection:
    # the time line is connecting
    if farmers[i].end > endConnection:
      endConnection = farmers[i].end
  else:
    # the time line is not connecting
    # found a time period where all farmers are milking milk
    milkPeriod = endConnection - startConnection
    if maxMilkPeriod < milkPeriod:
      maxMilkPeriod = milkPeriod

    noMilkPeriod = farmers[i].start - endConnection
    if maxNoMilkPeriod < noMilkPeriod:
      maxNoMilkPeriod = noMilkPeriod

    startConnection = farmers[i].start
    endConnection = farmers[i].end

milk2Output.write(f'{maxMilkPeriod} {maxNoMilkPeriod}\n')
