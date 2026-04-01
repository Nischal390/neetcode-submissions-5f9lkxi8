class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hash_map_s = {}
        hash_map_t = {}
        
        for c in s:
            if c in hash_map_s:
                hash_map_s[c]+=1
            else:
                hash_map_s[c]=1

        for c in t:
            if c in hash_map_t:
                hash_map_t[c]+=1
            else:
                hash_map_t[c]=1
        
        if hash_map_s == hash_map_t:
            return True

        return False