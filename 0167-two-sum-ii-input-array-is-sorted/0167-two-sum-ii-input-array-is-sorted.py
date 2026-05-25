class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target:
                return [lo + 1, hi + 1]   # 1-indexed
            elif s < target:
                lo += 1    # need bigger sum → move left pointer right
            else:
                hi -= 1    # need smaller sum → move right pointer left
        
        return []  # guaranteed to find answer