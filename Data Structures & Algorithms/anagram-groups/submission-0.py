class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        res = []
        for i in strs:
            word = "".join(sorted(i))
            print(word)
            if word in words:
                words[word].append(i)
            else:
                words[word] = [i]
        # print(words)
        new = sorted(words.items(), key=lambda item: len(item[1]))
        print(new)
        for v in words.values():
            res.append(v)
        return res



        
            

        