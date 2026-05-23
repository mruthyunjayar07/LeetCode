class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = sum(gas), sum(cost)
        
        if total_gas < total_cost:
            return -1
        
        current_gas = 0
        start = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        
        return start