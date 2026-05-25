class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            ba, bb, bc = a & 1, b & 1, c & 1
            if bc == 0:
                flips += ba + bb   # both must be 0; each 1 costs 1 flip
            else:
                flips += 1 if (ba | bb) == 0 else 0  # at least one must be 1
            a >>= 1; b >>= 1; c >>= 1
        return flips