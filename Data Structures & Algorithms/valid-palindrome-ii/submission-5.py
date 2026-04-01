class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(k):
            n = len(k)
            print(n)
            if n == 0:
                return True
            for i in range(n):
                if k[i] == k[-(i+1)]:
                    continue
                else:
                    return False
            return True
        l = len(s)
        for i in range(l):
            if s[i] == s[-(i+1)]:
                continue
            elif s[i] == s[-(i+2)]:
                j = l-(i+2)
                return isPalindrome(s[i:j+1])
            elif s[i+1] == s[-(i+1)]:
                j = l-(i+1)
                return isPalindrome(s[i+1:j+1])
            else:
                return False

        return True