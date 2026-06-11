from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        i=0
        j=1
        while j<len(prices):
            if prices[i]<prices[j]:
                res=max(res,prices[j]-prices[i])
            else:
                i=j
            j=j+1
        return res
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
