class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            count=[0]*26
            for x in s:
                count[ord(x)-ord('a')]+=1
            if tuple(count) not in res:
                res[tuple(count)]=[]
            res[tuple(count)].append(s)
        return list(res.values())
