class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        highest = 0
        score = 0
        dup = set()
        while right<len(s):
            if s[right] not in dup:
                dup.add(s[right])
                right +=1
                score = right-left
            else:
                dup.remove(s[left])
                left +=1
                score = right-left   
            highest = max(score,highest)
        return highest
                


        
