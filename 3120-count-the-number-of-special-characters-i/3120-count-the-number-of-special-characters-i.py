class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = upper = 0
        for c in word:
            if c.islower(): lower |= 1 << (ord(c) - ord('a'))
            else:           upper |= 1 << (ord(c) - ord('A'))
        return bin(lower & upper).count('1')