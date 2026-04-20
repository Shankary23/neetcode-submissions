class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            print(seen)
            if rem in seen:
                print("seen")
                return [seen[rem],i]
            else:
                seen[nums[i]] = i
        
        