"""
ID: alantao2
LANG: PYTHON3
PROG: namenum
"""

nameNumInput = open('namenum.in', 'r')
num = nameNumInput.readline().strip()
nameNumOutput = open('namenum.out', 'w')
dictionary = open('dict.txt', 'r')
length = len(num)

phonePad = {
  '2': ['A','B','C'],
  '3': ['D','E','F'],
  '4': ['G','H','I'],
  '5': ['J','K','L'],
  '6': ['M','N','O'],
  '7': ['P','R','S'],
  '8': ['T','U','V'],
  '9': ['W','X','Y']
}

# code...

# sorting dictionary
root_hash = {}
w = dictionary.readline().strip()
while w != '':
  currentHash = root_hash
  if len(w) == length:
    for char in w:
      if char not in currentHash:
        currentHash[char] = {}
      currentHash = currentHash[char]
  w = dictionary.readline().strip()


list = [-1] * length
word = [None] * length
hash = [None] * length
hash[0] = root_hash
cur = 0

while cur > -1:
  list[cur] += 1
  if list[cur] == 3:
    list[cur] = -1
    cur -= 1
    continue
  letter = phonePad[num[cur]][list[cur]]
  if letter in hash[cur]:
    word[cur] = letter
    if cur + 1 == length:
      # find one
      nameNumOutput.write(''.join(word) + '\n')
    else:
      hash[cur + 1] = hash[cur][letter]
      cur += 1
for c in word:
  if c == None:
    nameNumOutput.write('NONE\n')
    break