class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0
        
        for price in prices[1:]:
            hold = max(hold, cash - price)        # keep holding OR buy today
            cash = max(cash, hold + price - fee)  # keep cash OR sell today
        
        return cash