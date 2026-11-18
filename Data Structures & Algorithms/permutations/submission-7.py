class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(seen,path):
            if len(path) == len(nums):
                res.append(path)
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:continue
                back(seen.union([nums[i]]),path+[nums[i]])
        back(set(),[])
        return res
