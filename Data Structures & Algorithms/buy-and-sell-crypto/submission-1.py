class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        start = 0
        end = len(prices)-1

        while start<end:
            if prices[end] - prices[start] > maxprof:
                maxprof =  prices[end] - prices[start]
            start +=1
            end -=1
        return maxprof