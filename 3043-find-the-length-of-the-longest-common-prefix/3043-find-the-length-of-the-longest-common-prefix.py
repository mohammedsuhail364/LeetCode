class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen=set()
        for i in arr1:
            s=str(i)
            t=''
            for i in s:
                t+=i
                seen.add(t)
        res=0
        for i in arr2:
            s=str(i)
            t=''
            for i in s:
                t+=i
                if t in seen:
                    res=max(res,len(t))
        return res

        