class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0   # boundary of current jump
        farthest = 0      # farthest we can reach

        for i in range(len(nums) - 1):  # don't need to jump from last index
            farthest = max(farthest, i + nums[i])

            if i == current_end:        # exhausted current jump range
                jumps += 1
                current_end = farthest  # make the jump to farthest

        return jumps