def main(inputFile, outputFile):
  circleCrossInput = open(inputFile, 'r')
  circleCrossOutput = open(outputFile, 'w')
  circle = circleCrossInput.readline().strip()
  circle = [circle[i:i+1] for i in range(0, len(circle))]
  circleCrossInput.close()
  circleCrossOutput.write(str(getCrossPairs(circle)) + '\n')
  circleCrossOutput.close()

def getCrossPairs(circle: list):
  crossCount = 0
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  for i in range(0, len(alphabet)):
    for j in range(i + 1, len(alphabet)):
      checked = []
      for letter in circle:
        if letter == alphabet[i] or letter == alphabet[j]:
          checked.append(letter)
      curLetter = checked[0]
      notCrossPair = False
      for item in range(1, len(checked)):
        if checked[item] == curLetter:
          notCrossPair = True
          break
        curLetter = checked[item]
      if notCrossPair == False:
        crossCount += 1
      # print(alphabet[i] + '         ' + alphabet[j])
  return crossCount 

main('circlecross.in', 'circlecross.out')