class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)
        n = len(nums)
    
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo, hi = min(a, b), max(a, b)
        
            diff[2] += 2
            diff[2 * limit + 1] -= 2
        
            diff[lo + 1] -= 1
            diff[hi + limit + 1] += 1
        
            diff[a + b] -= 1
            diff[a + b + 1] += 1
    
        result = float('inf')
        curr = 0
        for T in range(2, 2 * limit + 1):
             curr += diff[T]
             result = min(result, curr)

        return result
        