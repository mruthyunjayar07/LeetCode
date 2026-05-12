class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        
        energy = 0
        for actual, minimum in tasks:
            energy = max(energy + actual, minimum)
        
        return energy