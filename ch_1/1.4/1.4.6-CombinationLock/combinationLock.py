"""
ID: alantao2
LANG: PYTHON3
PROG: combo
"""

comboInput = open('combo.in', 'r')
comboOutput = open('combo.out', 'w')

maxDial = int(comboInput.readline().strip())
johnComb = comboInput.readline().strip().split()
masterComb = comboInput.readline().strip().split()
dial = []
if maxDial <= 4:
  comboOutput.write(str(maxDial ** 3) + '\n')
else:
  for j in range(1, maxDial + 1):
    dial.append(j)
  dial.append(1)
  dial.append(2)
  dial.insert(0, maxDial)
  dial.insert(0, maxDial - 1)

  johnList = set()
  masterList = []
  combination = 125 + 125
  subtractCount = 1
  for i in range(0, 3):
    count = 0
    numJ = int(johnComb[i]) + 1
    numM = int(masterComb[i]) + 1
    johnList.add(dial[numJ])
    johnList.add(dial[numJ + 1])
    johnList.add(dial[numJ + 2])
    johnList.add(dial[numJ - 1])
    johnList.add(dial[numJ - 2])
    # masterList.append(dial[numM])
    if dial[numM] in johnList:
      count += 1
    # masterList.append(dial[numM + 1])
    if dial[numM + 1] in johnList:
      count += 1
    # masterList.append(dial[numM + 2])
    if dial[numM + 2] in johnList:
      count += 1
    # masterList.append(dial[numM - 1])
    if dial[numM - 1] in johnList:
      count += 1
    # masterList.append(dial[numM - 2])
    if dial[numM - 2] in johnList:
      count += 1
    subtractCount *= count
    johnList.clear()
    masterList.clear()
  comboOutput.write(str(combination - subtractCount) + '\n')