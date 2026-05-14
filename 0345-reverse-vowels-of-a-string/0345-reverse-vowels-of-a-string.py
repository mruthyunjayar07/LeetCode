class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        lo, hi = 0, len(s) - 1
        
        while lo < hi:
            while lo < hi and s[lo] not in vowels:
                lo += 1
            while lo < hi and s[hi] not in vowels:
                hi -= 1
            
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        
        return "".join(s)