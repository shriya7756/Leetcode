class Solution:
    def largestEven(self, s: str) -> str:
        
        while s and int(s[-1])!=2: 
            s=s[:-1] 
        return s
        
s=Solution()
print(s.largestEven("1221"))
