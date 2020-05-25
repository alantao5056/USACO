def main(inputFile, outputFile):
  hpsInput = open(inputFile, 'r')
  hpsOutput = open(outputFile, 'w')
  N = int(hpsInput.readline().strip())
  game = []
  for _ in range(0, N):
    line = hpsInput.readline().strip().split()
    if line[0] != line[1]:
      game.append(line)
  hpsInput.close()
  hpsOutput.write(str(getMostWin(game)) + '\n')
  hpsOutput.close()
  
def getMostWin(game: list) -> int:
  winCount_a = 0
  winCount_b = 0
  comb_a = {
    '1': '2',
    '2': '3',
    '3': '1'
  }
  
  comb_b = {
    '1': '3',
    '2': '1',
    '3': '2'
  }
  
  for g in game:
    firstCow = g[0]
    secondCow = g[1]
    if comb_a[firstCow] == secondCow:
      winCount_a += 1
    if comb_b[firstCow] == secondCow:
      winCount_b += 1
  if winCount_b > winCount_a:
    return winCount_b
  return winCount_a
      

main('hps.in', 'hps.out')