class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        
        if len(nums) != n + 1:
            return False
        
        freq = Counter(nums)
        
        if freq[n] != 2:
            return False
        
        for i in range(1, n):
            if freq[i] != 1:
                return False
        
        return True