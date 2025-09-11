class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=[]
        res=''
        for i in s:
            if i in "aeiouAEIOU":
                vowels.append(i)
        vowels.sort()
        x=0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                res+=vowels[x]
                x+=1
            else:
                res+=s[i]
        return res