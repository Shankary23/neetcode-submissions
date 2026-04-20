class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heaviest = float("-inf")
        while len(stones)>1:
            h1 = max(stones)
            stones.remove(h1)
            h2 = max(stones)
            stones.remove(h2)
            if h1<h2:
                h2 = h2-h1
                stones.append(h2)
            if h1 != h2:
                stones.append(h1 - h2)
        if stones:
            return stones[0]
        return 0
            

