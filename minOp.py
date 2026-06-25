class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        a=sum(nums)%k
        if a==0:
            return 0
        else:
            c=0
            nums.sort(reverse=True)
            for j in range(len(nums)):
                while nums[j]>0 and a>0:
                    c=c+1
                    nums[j]=nums[j]-1
                    a=a-1
                
                    if a==0:
                        return c
            return c
        
S=Solution()
print(S.minOperations([3,9,7],5))
