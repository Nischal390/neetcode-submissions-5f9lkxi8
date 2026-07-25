class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        chars= {}
        cur_len=max_len=0

        for i in range(n):
            chars[s[i]]=chars.get(s[i],0)+1
            cur_len+=1

            while chars[s[i]]>1:
                chars[s[l]]-=1
                cur_len-=1
                l+=1

            if cur_len>max_len:
                max_len = cur_len

        return max_len