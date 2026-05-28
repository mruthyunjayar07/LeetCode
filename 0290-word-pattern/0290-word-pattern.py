class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        
        p_to_w = {}
        w_to_p = {}
        
        for p, w in zip(pattern, words):
            if p in p_to_w:
                if p_to_w[p] != w: return False
            else:
                if w in w_to_p: return False  # word already mapped to diff char
                p_to_w[p] = w
                w_to_p[w] = p
        
        return True