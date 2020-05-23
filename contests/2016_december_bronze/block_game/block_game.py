alphabets = [0] * 26

def getCombCard(up: str, down: str):  
  upHash = [0] * 26
  downHash = [0] * 26
  for letter in up:
    upHash[ord(letter) - 97] += 1
  for letter in down:
    letterNum = ord(letter) - 97
    downHash[letterNum] += 1
    if downHash[letterNum] > upHash[letterNum]:
      upHash[letterNum] = downHash[letterNum]
  return upHash

def block_game(cards: list) -> list:
  alphabetHash = getCombCard(cards[0][0], cards[0][1])
  for i in range(1, len(cards)):
    curHash = getCombCard(cards[i][0], cards[i][1])
    for j in range(0, 26):
      alphabetHash[j] += curHash[j]
  return alphabetHash

blocksInput = open('blocks.in', 'r')
N = int(blocksInput.readline().strip())
cards = []
for _ in range(0, N):
	cards.append(blocksInput.readline().strip().split())

output = open('blocks.out', 'w')
alphabet = block_game(cards)
for letter in alphabet:
  output.write(str(letter) + '\n')
