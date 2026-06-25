class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=""
        for i in s:
            if i.isalnum():
                f+=i.upper()
        l=0
        r=len(f)-1
        while l<r:
          if f[l]!=f[r]:
            return False
          l=l+1
          r=r-1
        return True
            
s=Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))
            

