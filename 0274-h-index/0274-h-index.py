class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i, c in enumerate(citations):
            if c < i + 1:       # i+1 papers, but citation count dropped below
                return i
        
        return len(citations)   # all papers qualify