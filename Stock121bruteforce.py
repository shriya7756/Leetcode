from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      res=0
      for i in range(len(prices)-1):
          buy=min(prices[:i+1])
          
          for j in range(i+1,len(prices)-1):
              sell=max(prices[i+1:j+1])
              res=max(res,sell-buy)
      return res
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))

