def main(inputFile, outputFile):
  lifeguardsInput = open(inputFile, 'r')
  lifeguardsOutput = open(outputFile, 'w')
  N = int(lifeguardsInput.readline().strip())
  lifeguards = []
  for _ in range(0, N):
    line = lifeguardsInput.readline().strip().split()
    lifeguards.append([int(line[0]), int(line[1])])
  lifeguards.sort()
  # print(getTime(lifeguards))
  lifeguardsInput.close()
  lifeguardsOutput.write(str(getMaxTimeWhenFired(lifeguards)) + '\n')
  lifeguardsOutput.close()

def getMaxTimeWhenFired(lifeguards):
  total = lifeguards[0][1] - lifeguards[0][0]
  preActualTime = total
  minActualTime = total
  maxEnd = lifeguards[0][1]
  
  for i in range(1, len(lifeguards)):
    s = lifeguards[i][0]
    e = lifeguards[i][1]
    curActualTime = e - s
    
    # compare with pre(pre)
    preOverlap = getOverlap(s, e, lifeguards[i - 1][1])
    preActualTime -= preOverlap
    minActualTime = max(min(minActualTime, preActualTime), 0)
    
    # compare with all(current)
    allOverlap = getOverlap(s, e, maxEnd)
    curActualTime -= allOverlap
    maxEnd = max(maxEnd, e)
    
    preActualTime = curActualTime
    
    total += curActualTime
  
  return total - minActualTime
    
def getOverlap(s, e, preEnd):
  return max(min(e - s, preEnd - s), 0)