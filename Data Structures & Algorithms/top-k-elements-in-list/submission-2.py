class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        freq = Counter(nums)
        print(freq)
        sorted_freq = sorted(freq.items(),reverse = True, key=lambda item:item[1])
        new = dict(sorted_freq)
        res = []
        for key,v in new.items():
            print(key,v)
            if len(res) < k:
                res.append(key)
        return res


        