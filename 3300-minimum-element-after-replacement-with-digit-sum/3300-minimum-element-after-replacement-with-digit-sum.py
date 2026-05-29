from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = 100

        for x in nums:
            s = 0
            while x:
                s += x % 10
                x //= 10
            res = min(res, s)

        return res