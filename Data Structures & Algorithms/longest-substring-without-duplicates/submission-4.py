class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        l = len(s)
        char_hash_run = {}
        curr_count = 0
        curr_max = 0
        for i in range(l):
            char_hash_run[s[right]] = char_hash_run.get(s[right],0)+1
            if char_hash_run.get(s[right],0)>=2:
                while(char_hash_run[s[right]]>1):
                    char_hash_run[s[left]]-=1
                    left+=1
                    curr_count-=1
            
            right += 1
            curr_count+=1
            if curr_count>curr_max:
                curr_max = curr_count

        return curr_max