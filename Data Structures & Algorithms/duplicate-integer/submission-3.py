class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nondup = set(nums)
        return len(nondup) != len(nums)
        