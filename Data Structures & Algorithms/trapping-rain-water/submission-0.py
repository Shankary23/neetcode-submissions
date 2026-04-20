class Solution:
    def trap(self, height: List[int]) -> int:
        left_side = 0
        right_side = 0
        stored = 0
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n

        for i in range(n):
            j = -i -1
            max_left[i] = left_side
            max_right[j] = right_side
            left_side = max(left_side, height[i])
            right_side = max(right_side, height[j])

        for i in range(n):
            possible = min(max_left[i],max_right[i])
            stored += max(0, possible-height[i])
        return stored
    

