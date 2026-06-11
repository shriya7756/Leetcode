class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        
        res=0
        for i in range(len(s)):
            Set=set()
            for j in range(i+1,len(s)):
                if s[j] in Set:
                    break
                    
                Set.add(s[j])
                res=max(res,len(Set))
            
        return res
