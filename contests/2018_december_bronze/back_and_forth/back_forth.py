def main(inputFile, outputFile):
  backFourthInput = open(inputFile, 'r')
  backFourthOutput = open(outputFile, 'w')
  
  tank1Buckets = backFourthInput.readline().strip().split()
  tank1Buckets = list(map(int, tank1Buckets))
  
  tank2Buckets = backFourthInput.readline().strip().split()
  tank2Buckets = list(map(int, tank2Buckets))
  
  backFourthInput.close()
  
  backFourthOutput.write(str(getLenOfPossibleResults(tank1Buckets, tank2Buckets)) + '\n')
  backFourthOutput.close()
  
def getLenOfPossibleResults(lTankBuckets: list, rTankBuckets: list) -> int:
  lTank = 1000
  rTank = 1000
  combSet = set()
  
  for i in lTankBuckets:
    lTank1 = lTank + i
    rTank1 = rTank - i
    lTankBuckets1 = removeBucket(lTankBuckets, i)
    rTankBuckets1 = addBucket(rTankBuckets, i)
    for j in rTankBuckets1:
      lTank2 = lTank1 - j
      rTank2 = rTank1 + j
      lTankBuckets2 = addBucket(lTankBuckets1, j)
      rTankBuckets2 = removeBucket(rTankBuckets1, j)
      for k in lTankBuckets2:
        lTank3 = lTank2 + k
        rTank3 = rTank2 - k
        lTankBuckets3 = removeBucket(lTankBuckets2, k)
        rTankBuckets3 = addBucket(rTankBuckets2, k)
        for l in rTankBuckets3:
          lTank4 = lTank3 - l
          combSet.add(lTank4)
  return len(combSet)

def removeBucket(originalBuckets, bucket):
  newBuckets = originalBuckets.copy()
  newBuckets.pop(originalBuckets.index(bucket))
  return newBuckets

def addBucket(originalBuckets, bucket):
  newBuckets = originalBuckets.copy()
  newBuckets.append(bucket)
  return newBuckets
  
def move(itemIndex, arr1, arr2):
  arr2.append(arr1.pop(itemIndex))

main('backfourth.in', 'backfourth.out')