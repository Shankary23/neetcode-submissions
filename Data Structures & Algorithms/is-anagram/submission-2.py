class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = Counter(s)
        w2 = Counter(t)
        if len(w1)!= len(w2):
            return False
        for k,v in w1.items():
            if w2[k] != w1[k]:
                return False
        return True
        