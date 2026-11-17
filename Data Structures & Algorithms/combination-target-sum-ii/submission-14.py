class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index,cur_sum,path):
            if cur_sum == target:
                res.append(path)
                return

            if cur_sum>target: return

            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]: continue
                backtrack(i+1,cur_sum+candidates[i],path+[candidates[i]])

        backtrack(0,0,[])
        return res