class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]

        def backtrack(i,path,cur):
            if cur == target:
                res.append(path.copy())
                return
            
            if cur>target or i>=len(nums):
                return

            path.append(nums[i])
            backtrack(i,path,cur+nums[i])
            path.pop()

            backtrack(i+1,path,cur)

        backtrack(0,[],0)
        return res