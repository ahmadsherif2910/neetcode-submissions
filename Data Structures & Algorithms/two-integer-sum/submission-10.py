class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in val:
                val[num] = [nums.count(num), []]
        
            val[num][1].append(i)
        print(val)
        for key,value in val.items():
            if (target-key == key and value[0]>1):
                return [value[1][0],val[target-key][1][1]]
            elif (target-key != key and target-key in val) :
                return [value[1][0],val[target-key][1][0]]

