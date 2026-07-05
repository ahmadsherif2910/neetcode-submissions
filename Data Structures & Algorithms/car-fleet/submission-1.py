class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged = list(zip(position, speed))
        merged.sort()
        fleet = 1
        time = (target - merged[-1][0])/merged[-1][1]
        for i in range(len(merged) - 2, -1, -1):
            if ((target - merged[i][0])/merged[i][1])>time:
                time = (target - merged[i][0])/merged[i][1]
                fleet+=1
        return fleet


        