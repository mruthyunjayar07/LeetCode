class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            hours = sum(ceil(p / mid) for p in piles)

            if hours <= h:
                hi = mid      # mid works, try slower
            else:
                lo = mid + 1  # too slow, go faster

        return lo