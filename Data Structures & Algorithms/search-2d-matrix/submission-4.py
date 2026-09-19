class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binsearch(array):
            start = 0
            end = len(array)-1

            while start<= end:
                mid = (start+end)//2
                if array[mid] == target:
                    return True
                elif array[mid]<target:
                    start = mid+1
                else:
                    end = mid -1
            return False
        for i in matrix:
            print(i[0],i[-1],i)
            if i[0] <= target and target <= i[-1]:
                print("test")
                res = binsearch(i)
                if res == True:
                    return True
        
        return False