class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        
        for c1, c2 in zip(word1, word2):
            result.append(c1)
            result.append(c2)
        
        result.append(word1[len(word2):])
        result.append(word2[len(word1):])
        
        return "".join(result)