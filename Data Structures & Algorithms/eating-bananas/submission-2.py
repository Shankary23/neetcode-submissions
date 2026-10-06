import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        m = max(piles)
        
        if h == len(piles):
            return m
        pot = float('inf')
        while start <= m:
            mid = (start+m)//2
            hour = h
            for i in piles:
                hour -= math.ceil(i/mid)
            
            if hour < 0:
                start = mid+1
            else:
                pot = min(mid, pot)
                m = mid-1
        return pot

                


        