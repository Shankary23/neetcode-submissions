class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        freq = Counter(nums)
        print(freq)
        res = []
        for key,v in freq.items():
            if v >= k:
                res.append(key)
        return res


        