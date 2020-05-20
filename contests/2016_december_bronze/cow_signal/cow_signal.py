def enlarge(line: list, K: int) -> list:
  firstEle = line[0]
  newLine = []
  curChar = firstEle
  for e in range(0, K):
    newLine.append(firstEle)
  for i in range(1, len(line)):
    curEle = line[i]
    if curEle == curChar:
      for j in range(0, K):
        newLine.append(curEle)
    else:
      curChar = curEle
      for l in range(0, K):
        newLine.append(curEle)
  return newLine


def amplifySignal(signal: list) -> list:
  newList = []
  for line in signal:
    enlargedList = enlarge(line, K)
    for k in range(0, K):
      newList.append(enlargedList)
  return newList

input = open('cowsignal.in', 'r')
M, N, K = [int(x) for x in input.readline().split()]
signal = []
for _ in range(M):
  signal.append(list(input.readline().strip()))
input.close()

amplifiedSignal = amplifySignal(signal)
print(amplifiedSignal)
output = open('cowsignal.out', 'w')
for line in amplifiedSignal:
  output.write("".join(line) + "\n")
output.close()