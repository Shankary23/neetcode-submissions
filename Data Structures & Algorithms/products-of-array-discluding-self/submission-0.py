class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            sum = 1
            for j in range(0,len(nums)):
                
                if i!=j:
                    sum *= nums[j]
            res.append(sum)
        return res