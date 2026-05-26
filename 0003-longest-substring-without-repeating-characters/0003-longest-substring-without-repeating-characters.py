class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}   # char → last seen index
        res = lo = 0
        
        for hi, c in enumerate(s):
            if c in last and last[c] >= lo:
                lo = last[c] + 1        # jump left pointer past duplicate
            last[c] = hi
            res = max(res, hi - lo + 1)
        
        return res