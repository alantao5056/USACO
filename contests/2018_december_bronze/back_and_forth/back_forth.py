def getAllPossibleComb(firstBuckets: list, secondBuckets: list) -> str:
  fTank = 1000
  sTank = 1000
  comb = set()
  for i in range(0, len(firstBuckets)):
    bucket = int(firstBuckets[i])
    secondBuckets.append(firstBuckets.pop(i))
    fTank -= bucket
    sTank += bucket
    for j in range(0, len(secondBuckets)):
      bucket = int(secondBuckets[j])
      firstBuckets.append(secondBuckets.pop(j))
      sTank -= bucket
      fTank += bucket
      for k in range(0, len(firstBuckets)):
        bucket = int(firstBuckets[k])
        secondBuckets.append(firstBuckets.pop(k))
        fTank -= bucket
        sTank += bucket
        for l in range(0, len(secondBuckets)):
          if l == 0:
            fOrig = fTank
            sOrig = sTank
            fBuck = firstBuckets
            sBuck = secondBuckets
          fTank = fOrig
          sTank = sOrig
          firstBuckets = fBuck
          secondBuckets = sBuck
          bucket = int(secondBuckets[l])
          firstBuckets.append(secondBuckets.pop(l))
          sTank -= bucket
          fTank += bucket
          print(fTank)
          print(sTank)

getAllPossibleComb([1, 1, 1, 1, 1, 1, 1, 1, 1, 2], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
