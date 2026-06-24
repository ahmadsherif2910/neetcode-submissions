class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = {num:nums.count(num) for num in nums}
        print(hsh)
        hsh = dict(sorted(hsh.items(), key=lambda item: item[1],reverse = True))
        print(hsh)
        return list(hsh)[:k]
