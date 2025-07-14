class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        word=s.replace('-',"")
        extra=len(word)%k
        res=[]
        if extra:
            res.append(word[:extra])
        for i in range(extra,len(word),k):
            res.append(word[i:i+k])
        return '-'.join(res).upper()