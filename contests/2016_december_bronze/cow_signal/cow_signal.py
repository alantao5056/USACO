def amplifySignal(signal: list) -> list:
  return []

input = open('cowsignal.in', 'r')
M, N, K = [int(x) for x in input.readline().split()]
signal = []
for _ in range(M):
  signal.append(list(input.readline().strip()))
input.close()

amplifiedSignal = amplifySignal(signal)
output = open('cowsignal.out', 'w')
output.writelines(amplifiedSignal)
output.close
