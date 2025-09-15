class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s=text.split()
        flag=[True]*len(s)
        for i in brokenLetters:
            for x in range(len(s)):
                word=s[x]
                if i in word and flag[x]:
                    flag[x]=False
        return flag.count(True)