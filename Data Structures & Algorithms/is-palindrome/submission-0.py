class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        for i in range(len(s)):
            if s[-(i+1)] == s[i]:
                continue
            else:
                return False
        return True
