class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letter_map = Counter(s1)
        l,r=0,0
        while l <= len(s2)-len(s1):
            if s2[l] not in letter_map:
                l+=1
                r=1
            elif s2[l] in letter_map:
                map_copy = letter_map.copy()
                r=l
                for _ in range(len(s1)):
                    map_copy[s2[r]]-=1
                    if map_copy[s2[r]]<0:
                        l+=1
                        r=l
                        break
                    r+=1
                else:
                    if all(value == 0 for value in map_copy.values()):
                        return True
                    l+=1
                    r=l

        return False