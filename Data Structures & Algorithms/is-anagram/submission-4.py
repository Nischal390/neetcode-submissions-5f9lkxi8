class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}

        for c in s:
            hash_map1[c] = hash_map1.get(c,0) + 1

        for c in t:
            hash_map2[c] = hash_map2.get(c,0)+1

        
        if hash_map1 == hash_map2:
            return True

        return False
