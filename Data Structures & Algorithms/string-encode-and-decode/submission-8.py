class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            word_len = len(i)
            res+= str(word_len) + "$"
            res+= i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        if not s:
            return [""]
        i = 0
        j = 0
        while i< len(s):
            j=i
            while s[j] != "$":
                j+=1
            pos = int(s[i:j])
            word+= s[j+1 : j+1+pos]
            res.append(word)
            i = j+1 + pos
            word = ""
        return res



        
