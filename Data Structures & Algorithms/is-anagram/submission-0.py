class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sm = {}
        tm ={}
        for i in s:
            if i not in sm:
                sm[i] =1
            else:
                sm[i]+=1
        for j in t:
            if j not in tm:
                tm[j] = 1
            else:
                tm[j]+=1
        if sm == tm:
            return True
        return False 

