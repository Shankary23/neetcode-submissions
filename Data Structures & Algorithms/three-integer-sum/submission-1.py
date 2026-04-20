class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
       
        for pointer in range(len(nums)):
            if pointer > 0 and nums[pointer] == nums[pointer - 1]:
                continue
            start = pointer+1
            end = len(nums)-1
            while start<end:
                if nums[pointer] + nums[start]+nums[end] == 0:
                    res.append([nums[pointer],nums[start],nums[end]])
                    start +=1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    end -=1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif nums[pointer]+ nums[start]+nums[end]<0:
                    start+=1
                elif nums[pointer]+ nums[start]+nums[end]>0:
                    end -=1
        return res
                

