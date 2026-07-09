class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        res = []
        new = Counter(nums)
        new = dict(new)
        new = sorted(new.items(), key = lambda item: -item[1])
        print(new)
        for i,j in new:
            print(i,j)
            if k != 0:
                res.append(i)
                k-=1
        return res
            


        