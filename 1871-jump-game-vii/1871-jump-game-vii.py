class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        
        dp = [False] * n
        dp[0] = True
        
        prefix = [0] * (n + 1)
        prefix[1] = 1
        
        for i in range(1, n):
            if s[i] == '0':
                lo = max(0, i - maxJump)
                hi = i - minJump
                if hi >= 0 and prefix[hi + 1] - prefix[lo] > 0:
                    dp[i] = True
            prefix[i + 1] = prefix[i] + (1 if dp[i] else 0)
        
        return dp[-1]