from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        max_cost=max(cost)
        max_cost_idx=cost.index(max_cost)
        #keep max_cost_idx+1, del remaining
        print(s[max_cost_idx])
      
s=Solution()
s.minCost("aabaac",[1,2,3,4,1,10])
