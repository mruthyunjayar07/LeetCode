class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0  

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert] = nums[i]
                insert += 1

        for i in range(insert, len(nums)):
            nums[i] = 0