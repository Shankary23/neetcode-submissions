class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dup = nums[0]
        for i in range(1,len(nums)):
            dup = dup^nums[i]
        return dup