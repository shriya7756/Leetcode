class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
                cursum=numbers[l]+numbers[r]
                if numbers[r]==target-numbers[l]:
                    return [l+1,r+1]
                elif cursum<target:
                    l=l+1
                else:
                    r=r-1
