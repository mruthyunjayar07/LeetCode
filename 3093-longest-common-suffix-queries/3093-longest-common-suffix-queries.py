class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        trie = [{}, -1]
        
        def is_better(new_idx, cur_idx):
            if cur_idx == -1: return True
            nw, cw = len(wordsContainer[new_idx]), len(wordsContainer[cur_idx])
            return nw < cw or (nw == cw and new_idx < cur_idx)
        
        for idx, word in enumerate(wordsContainer):
            node = trie
            if is_better(idx, node[1]):
                node[1] = idx
            for ch in reversed(word):
                if ch not in node[0]:
                    node[0][ch] = [{}, -1]
                node = node[0][ch]
                if is_better(idx, node[1]):
                    node[1] = idx
        
        res = []
        for word in wordsQuery:
            node = trie
            for ch in reversed(word):
                if ch not in node[0]:
                    break
                node = node[0][ch]
            res.append(node[1])
        
        return res