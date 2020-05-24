def main(inputFile, outputFile):
  cowtipInput = open(inputFile, 'r')
  cowtipOutput = open(outputFile, 'w')
  N = int(cowtipInput.readline().strip())
  grid = []
  for _ in range(0, N):
    line = []
    readline = cowtipInput.readline().strip()
    for cow in readline:
      line.append(cow)
    grid.append(line)
  cowtipInput.close()
  cowtipOutput.write(str(getNumOfTip(grid)) + '\n')
  cowtipOutput.close()

def flip(grid, x, y):
  for i in range(0, x + 1):
    for j in range(0, y + 1):
      if grid[i][j] == '0':
        grid[i][j] = '1'
      else:
        grid[i][j] = '0'

def getNumOfTip(grid: list) -> int:
  count = 0
  for i in range(len(grid) - 1, -1, -1):
    for j in range(i, -1, -1):
      if grid[i][j] == '1':
        flip(grid, i, j)
        count += 1
      if grid[j][i] == '1':
        flip(grid, j, i)
        count += 1
  return count

main('cowtip.in', 'cowtip.out')