class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sub in (matrix):
            if sub[-1]>target:
                if target in sub:
                    return True
        return False
        