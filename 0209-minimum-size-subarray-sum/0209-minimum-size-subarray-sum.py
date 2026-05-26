class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lo = curr_sum = 0
        res = float('inf')
        
        for hi in range(len(nums)):
            curr_sum += nums[hi]
            while curr_sum >= target:
                res = min(res, hi - lo + 1)
                curr_sum -= nums[lo]
                lo += 1
        
        return res if res != float('inf') else 0