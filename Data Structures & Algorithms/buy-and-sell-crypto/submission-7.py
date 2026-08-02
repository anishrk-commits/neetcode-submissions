class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_return = 0

        if len(prices) <= 1:
            return 0
        
        left = 0
        right = 1
        
        while right < len(prices):
            current = prices[right] - prices[left]
            if current <= 0:
                left = right
                right += 1
            elif current > max_return:
                max_return = current
                right += 1
            else:
                right += 1

        return max_return
            