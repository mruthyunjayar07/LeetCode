class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle k > n (e.g. k=10, n=7 → same as k=3)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)   # Step 1: reverse entire array
        reverse(0, k - 1)   # Step 2: reverse first k elements
        reverse(k, n - 1)   # Step 3: reverse remaining elements