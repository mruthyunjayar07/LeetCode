class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid          # peak is on the left side (inclusive)
            else:
                lo = mid + 1      # peak is on the right side
        
        return lo