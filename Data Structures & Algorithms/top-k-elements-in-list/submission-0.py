class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] =1
            else:
                freq[i] +=1
        sort = sorted(freq.items(),key=lambda item:item[1], reverse = True)
        sort = dict(sort)
        res = []
        for key, val in sort.items():
            if k>0:
                res.append(key)
                k-=1
        return res
            

            
