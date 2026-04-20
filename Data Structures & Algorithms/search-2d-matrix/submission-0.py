class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sub in (matrix):
            if target in sub:
                return True
            # if sub[-1]>target:
        return False
        