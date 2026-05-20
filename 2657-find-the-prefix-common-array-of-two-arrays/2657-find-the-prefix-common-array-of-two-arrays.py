class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = []
        seen_A = set()
        seen_B = set()
        count = 0
        
        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])
            
            if A[i] in seen_B:
                count += 1
            if B[i] in seen_A and B[i] != A[i]:
                count += 1
            
            C.append(count)
        
        return C