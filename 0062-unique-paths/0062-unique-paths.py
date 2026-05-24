class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n  # base case: top row all 1s
        
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]  # dp[j] = from above + from left
        
        return dp[n-1]