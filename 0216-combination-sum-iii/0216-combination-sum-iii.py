class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, curr, total):
            if total > n or len(curr) > k:
                return
            
            if len(curr) == k and total == n:
                res.append(curr[:])
                return
            
            for num in range(start, 10):
                curr.append(num)
                backtrack(num + 1, curr, total + num)
                curr.pop()
        
        backtrack(1, [], 0)
        return res