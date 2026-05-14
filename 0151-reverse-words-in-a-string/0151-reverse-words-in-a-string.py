class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        lo, hi = 0, len(words) - 1
        while lo < hi:
            words[lo], words[hi] = words[hi], words[lo]
            lo += 1
            hi -= 1
        
        return " ".join(words)