class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[False]*len(s) for i in range(n)]
        count = 0

        for length in range(1,n+1):
            for i in range(n-length+1):
                j = i+length-1
                if j==i:
                    dp[i][j] = True
                    count+=1
                elif j-i == 1:
                    if s[i]==s[j]:
                        dp[i][j] = True
                        count+=1
                elif s[j]==s[i] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count+=1

        return count