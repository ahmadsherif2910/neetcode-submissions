class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            j=i+1
            while j<len(heights):
                tmp = min(heights[i],heights[j])*(j-i)
                res=max(res,tmp)
                j+=1
        return res
            
        