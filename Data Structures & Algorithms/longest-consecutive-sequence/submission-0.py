class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0
        for i in n:
            if i-1 not in n:
                next_num = i+1
                length = 1
                while next_num in n:
                    length+=1
                    next_num +=1
                longest = max(longest, length)
        return longest