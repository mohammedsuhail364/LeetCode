class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        di={}
        for i,src,tar in zip(indices,sources,targets):
            if s[i:i+len(src)]==src:
                di[i]=(len(src),tar)
        print(di)
        i=0
        res=[]
        while i<len(s):
            if i in di:
                length,target=di[i]
                res.append(target)
                i+=length
            else:
                res.append(s[i])
                i+=1
        return ''.join(res)