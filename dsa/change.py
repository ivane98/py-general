def recMC(coinValueList,change, knownResults):
   minCoins = change
   if change in coinValueList:
     knownResults[change] = 1
     return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i, knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recMC([1,5,8,10,25],33, [0]*64))