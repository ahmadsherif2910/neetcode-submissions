class Solution:

    def encode(self, strs: List[str]) -> str:
        tmp = ""
        for s in strs:
            tmp+= str(len(s))+"#"+s
        return tmp
            


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            res.append(s[j+1:j+1+l])
            i=j+1+l
        return res




        # if len(s) == 0:
        #     return [""]

        # res = []
        # for i in range(len(s)):
        #     x,s = int(s[0]),s[1:]
        #     # for j in range(int(x)):
        #     res.append(s[0:x])

