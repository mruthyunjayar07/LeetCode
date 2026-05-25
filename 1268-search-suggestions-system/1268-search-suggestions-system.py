from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        
        for ch in searchWord:
            prefix += ch
            lo = bisect_left(products, prefix)
            res.append([
                p for p in products[lo:lo+3] 
                if p.startswith(prefix)
            ])
        
        return res