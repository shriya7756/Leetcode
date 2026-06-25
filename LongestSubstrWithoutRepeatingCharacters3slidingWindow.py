class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        res=0
        Set=set()
        for j in range(len(s)):
            while s[j] in Set:
                Set.remove(s[i])
                i=i+1
            Set.add(s[j])
            res=max(res,j-i+1)
            
        return res

