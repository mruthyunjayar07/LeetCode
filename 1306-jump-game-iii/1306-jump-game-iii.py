class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not (0 <= start < len(arr)) or arr[start] < 0:
            return False
        if arr[start] == 0:
            return True

        arr[start] = -arr[start]  
        return (self.canReach(arr, start + arr[start]) or
                self.canReach(arr, start - arr[start]))