class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        elif len(s)==2 and s[0]!=s[1]:
            return 2

        l,r = 0,0
        x = set()
        x.add(s[l])
        x.add(s[r])
        res = 1
        while r<len(s)-1:
            r = r+1
            if s[r] not in x:
                res = max(res,r-l+1)
                x.add(s[r])
            else:
                while s[r]!=s[l]:
                    x.remove(s[l])
                    l+=1
                if s[r] == s[l]:
                    l+=1
        return res




        
        