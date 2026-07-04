class Solution:
    def dailyTemperatures(self, tmp: List[int]) -> List[int]:
        res = [0]*len(tmp)
        for i in range(len(tmp)):
            x=0
            for j in range(len(tmp[i+1:])+1):
                if tmp[j+i]<=tmp[i]:
                    x+=1
                elif tmp[j+i]>tmp[i]:
                    res[i]=x
                    break
        return res


