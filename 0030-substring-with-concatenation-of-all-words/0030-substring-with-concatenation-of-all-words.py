class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        
        w = len(words[0])      # word length
        k = len(words)         # number of words
        total = w * k          # window size
        need = Counter(words)
        res = []

        for offset in range(w):
            window = Counter()
            count = 0            # valid words in current window
            lo = offset
            
            for hi in range(offset, len(s) - w + 1, w):
                word = s[hi:hi + w]
                
                if word in need:
                    window[word] += 1
                    count += 1
                    while window[word] > need[word]:
                        left_word = s[lo:lo + w]
                        window[left_word] -= 1
                        count -= 1
                        lo += w
                    if count == k:
                        res.append(lo)
                else:
                    window.clear()
                    count = 0
                    lo = hi + w
        
        return res