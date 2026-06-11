class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxarea=0
        while l<r:
            maxarea=max(maxarea,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return maxarea
