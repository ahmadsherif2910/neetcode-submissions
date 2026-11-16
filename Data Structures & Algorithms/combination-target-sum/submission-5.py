class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index,cur_sum,path):
            if cur_sum == target:
                res.append(path)
                return

            if cur_sum>target: return

            for i in range(index,len(nums)):
                backtrack(i,cur_sum+nums[i],path+[nums[i]])

        backtrack(0,0,[])
        return res