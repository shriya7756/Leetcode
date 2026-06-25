class Solution:
    def rearrangeArray(self,nums: list[int]) -> list[int]:
        n=[]
        p=[]
        a=[]
        for i in range(0,len(nums)):
            if nums[i]<0:
                n.append(nums[i])
            if nums[i]>0:
                p.append(nums[i])
        
        for j in range(0,len(nums)//2):
            a.append(p[j])
            a.append(n[j])
        return a
nums=[-2,-9,5,-8,6,2]
s=Solution()
print(s.rearrangeArray(nums))
