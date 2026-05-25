class Trie:
    __slots__ = ['children', 'is_end']  # memory optimization
    
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, s: str):        # shared helper — no code duplication
        node = self
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node