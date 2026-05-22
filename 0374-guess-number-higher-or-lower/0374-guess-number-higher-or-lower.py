class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid          # found it!
            elif result == -1:
                right = mid - 1     # guess too high → go lower
            else:
                left = mid + 1      # guess too low  → go higher