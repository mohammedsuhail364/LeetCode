class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         longprefix=strs[0]
         for x in strs:
             i=0
             while i<len(longprefix) and i<len(x) and longprefix[i]==x[i]:
                 i+=1
             longprefix=longprefix[:i]
         return longprefix