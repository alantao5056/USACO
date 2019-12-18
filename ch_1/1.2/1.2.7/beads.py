"""
ID: alantao2
LANG: PYTHON3
PROG: beads
"""

beadsInput = open('beads.in', 'r')
beadsOutput = open('beads.out', 'w')
beadsInput.readline()
line = str(beadsInput.readline().strip())
beads = line + line
beadsNum = len(beads)

currentColor = ""
leftWLength = 0
leftLeftWLength = 0
wCounter = 0
counter = 0
maxLength = 0
leftLength = 0

# find first letter that is not a 'w'
for i in range (0, beadsNum):
  counter += 1
  if beads[i] != 'w':
    currentColor = beads[i]
    break

for i in range(counter, beadsNum):
  if beads[i] == currentColor:
    counter += 1
    wCounter = 0
  elif beads[i] == 'w':
    wCounter += 1
    counter += 1
  else:
    # print(f"{currentColor} - {counter} number of White: {wCounter}")
    currentColor = beads[i]
    # print(f"{counter} {leftLength} {leftLeftWLength}")
    length = counter + leftLength + leftLeftWLength
    if length > maxLength:
      maxLength = length
    
    leftLength = counter
    counter = 1
    leftLeftWLength = leftWLength
    leftWLength = wCounter
    wCounter = 0

length = counter + leftLength + leftLeftWLength
if length > maxLength:
  maxLength = length

if maxLength > len(line):
  maxLength = len(line)

beadsOutput.write(f'{maxLength}\n')
