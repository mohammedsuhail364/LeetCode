class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res=[]
        for word in dictionary:
            i=0
            j=0
            while i<len(s) and j<len(word):
                if s[i]==word[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j==len(word):
                res.append(word)
        di=defaultdict(list)
        for r in res:
            di[len(r)].append(r)
        if di:
            max_val=max(di)
            tmp=di[max_val]
            tmp.sort()
            if tmp:
                return tmp[0]
        return ""