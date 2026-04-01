#import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        #s = re.sub(r'[^A-Za-z0-9]','',s)
        s = s.lower()

        n = len(s)
        for i in range(n//2):
            if s[i]==s[-(i+1)]:
                continue
            else:
                return False

        return True