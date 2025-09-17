class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res=[]
        def is_subsequence(word):
            i=0
            j=0
            while i<len(s) and j<len(word):
                if s[i]==word[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            return j==len(word)
        best=""
        for word in dictionary:
            if is_subsequence(word):
                if len(word)>len(best) or (len(word)==len(best) and word<best):
                    best=word
        return best