class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        dp = [[False]*len(s) for i in range(n)]
        res = s[0]

        for length in range(1,n+1):
            for i in range(n-length+1):
                j = i+length-1
                if j==i:
                    dp[i][j] = True
                elif j-i == 1:
                    if s[i]==s[j]:
                        dp[i][j] = True
                elif s[j]==s[i] and dp[i+1][j-1]:
                    dp[i][j] = True
                if dp[i][j] and len(s[i:j+1])>len(res):
                    res = s[i:j+1]

        return res