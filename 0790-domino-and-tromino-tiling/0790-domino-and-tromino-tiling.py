class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        
        prev3, prev2, prev1 = 1, 2, 5
        
        for i in range(4, n + 1):
            curr = (2 * prev1 + prev3) % MOD
            prev3, prev2, prev1 = prev2, prev1, curr
        
        return prev1