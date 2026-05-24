class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        prev = list(range(n + 1))
        
        for i in range(1, m + 1):
            curr = [i] + [0] * n   # converting word1[:i] to "" costs i deletions
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]              # chars match → free
                else:
                    curr[j] = 1 + min(
                        prev[j],      # delete from word1
                        curr[j-1],    # insert into word1
                        prev[j-1]     # replace
                    )
            prev = curr
        
        return prev[n]