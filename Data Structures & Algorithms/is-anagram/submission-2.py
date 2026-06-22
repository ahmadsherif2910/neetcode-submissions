class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return {letter:s.count(letter) for letter in s } == {letter:t.count(letter) for letter in t } 