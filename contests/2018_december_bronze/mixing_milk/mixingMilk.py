from __future__ import annotations

class Bucket:
  def __init__(self, volume, amount):
    self.volume = volume
    self.amount = amount
  
  def pour(self):
    if self.amount + self.target.amount > self.target.volume:
      self.amount -= self.target.volume - self.target.amount
      self.target.amount = self.target.volume
    else:
      self.target.amount += self.amount
      self.amount = 0
  
  def setTarget(self, bucket: Bucket):
    self.target = bucket

def main(inputFile, outputFile):
  mixMilkInput = open(inputFile, 'r')
  mixMilkOutput = open(outputFile, 'w')

  buckets = list(map(parseBucket, mixMilkInput.read().splitlines()))
  
  mixMilkInput.close()
  
  results = getMilkAmounts(buckets[0], buckets[1], buckets[2])
  for result in results:
    mixMilkOutput.write(str(result) + '\n')
    
  mixMilkOutput.close()
  
def parseBucket(line: str) -> Bucket:
  parts = line.split()
  return Bucket(int(parts[0]), int(parts[1]))
  
def getMilkAmounts(b1, b2, b3):
  b1.setTarget(b2)
  b2.setTarget(b3)
  b3.setTarget(b1)
  
  currentBucket = b1
  for _ in range(0, 100):
    currentBucket.pour()
    currentBucket = currentBucket.target
    
  return [b1.amount, b2.amount, b3.amount]

main('mixmilk.in', 'mixmilk.out')