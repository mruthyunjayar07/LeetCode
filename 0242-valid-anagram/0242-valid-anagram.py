class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        count = [0] * 26
        for cs, ct in zip(s, t):
            count[ord(cs) - 97] += 1
            count[ord(ct) - 97] -= 1
        
        return all(x == 0 for x in count)