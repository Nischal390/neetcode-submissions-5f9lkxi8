class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        chars = {}
        curr_count=0
        max_count=0

        for i in range(n):
            curr_count+=1
            chars[s[i]]=chars.get(s[i],0)+1
            while chars[s[i]]>1:
                chars[s[l]]-=1
                l+=1
                curr_count-=1

            if curr_count>max_count:
                max_count = curr_count

        return max_count