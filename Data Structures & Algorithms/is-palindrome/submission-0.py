class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        word = "".join(char.lower() for char in s if char.isalnum())
        
        start = 0
        end = len(word)-1

        while start<= end:
            if word[start] != word[end]:
                return False
            start +=1
            end -=1
        return True

