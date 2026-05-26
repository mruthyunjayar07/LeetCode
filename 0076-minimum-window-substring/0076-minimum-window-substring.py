class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        need = Counter(t)
        have, required = 0, len(need)   # unique chars to satisfy
        window = {}
        lo = 0
        res_len, res_lo = float('inf'), 0
        
        for hi, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                if hi - lo + 1 < res_len:
                    res_len = hi - lo + 1
                    res_lo = lo
                window[s[lo]] -= 1
                if s[lo] in need and window[s[lo]] < need[s[lo]]:
                    have -= 1
                lo += 1
        
        return s[res_lo:res_lo + res_len] if res_len != float('inf') else ""