def main(inputFile: str, outputFile: str):
  outofplaceInput = open(inputFile, 'r')
  outofplaceOutput = open(outputFile, 'w')
  N = int(outofplaceInput.readline().strip())
  heights = []
  for _ in range(0, N):
    heights.append(int(outofplaceInput.readline().strip()))
  outofplaceInput.close()
  outofplaceOutput.write(str(getNumberOfSwaps(heights)) + '\n')
  outofplaceOutput.close()

def getNumberOfSwaps(heights: list) -> int:
  count = 0
  sortedHeights = sorted(heights)
  for i in range(0, len(heights) - 1):
    if heights == sortedHeights:
      return count
    minNumIndex = i
    for j in range(len(heights) - 1, i - 1, -1):
      if heights[j] < heights[minNumIndex]:
        minNumIndex = j
    if minNumIndex != i:
      heights[i], heights[minNumIndex] = heights[minNumIndex], heights[i]
      count += 1
  return count

main('outofplace.in', 'outofplace.out')