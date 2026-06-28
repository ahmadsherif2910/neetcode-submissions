class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res=0

        for num in numset:
            if num-1 not in numset:
                curr = num
                x=1
                while curr+1 in numset:
                    curr+=1
                    x+=1
                res = max(res,x)
        return res
            