def main(inputFile, outputFile):
  tamingInput = open(inputFile, 'r')
  tamingOutput = open(outputFile, 'w')
  
  N = int(tamingInput.readline().strip())
  log = tamingInput.readline().strip().split()
  
  log = list(map(int, log))
  
  tamingInput.close()
  tamingOutput.write(getMinMaxDay(log) + '\n')
  tamingOutput.close()  
def getMinMaxDay(log: list) -> str:
  # making a list to log all the dates
  # if we are not sure: False
  # if we are sure: True
  # if we know nothing happened on that day: 0
  
  certain = [False] * len(log)
  for i in range(0, len(log)):
    if log[i] != -1:
      certain[i] = -1
      certain[i - log[i]] = True
      for j in range(i - log[i] + 1, i):
        if certain[j] == True:
          return '-1'
        certain[j] = -1
  
  certain[0] = True
  
  small = 0
  big = 0
  for day in certain:
    if day == True:
      small += 1
    if day == False:
      big += 1
  return f'{small} {small + big}'

main('taming.in', 'taming.out')