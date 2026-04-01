class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = Counter(s)
        mp2 = Counter(t)

        return mp1==mp2