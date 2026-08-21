class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        smallest = float("inf")
        for i in range(len(prices)):
            if smallest > prices[i]:
                smallest = prices[i]
            elif max_prof< prices[i] - smallest:
                max_prof = prices[i] - smallest
        return max_prof

        

