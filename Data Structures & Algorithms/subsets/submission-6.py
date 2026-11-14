class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index):
            if index>=len(nums):
                res.append(path[:])
                return

            backtrack(index+1)

            path.append(nums[index])
            backtrack(index+1)
            path.pop()
        backtrack(0)
        return res