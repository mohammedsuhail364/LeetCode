class Solution:
    def equalFrequency(self, word: str) -> bool:
        res=[True]*len(word)
        for i in range(len(word)):
            new_word=word[:i]+word[i+1:]
            c=Counter(new_word)
            temp=max(c.values())
            for x,j in c.items():
                if j!=temp:
                    res[i]=False
        for i in res:
            if i:
                return True
        return False