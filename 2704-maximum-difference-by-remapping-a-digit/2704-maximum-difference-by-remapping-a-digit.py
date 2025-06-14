class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=list(str(num))
        large=list(str(num))
        small=list(str(num))
        
        min_val=0
        max_val=s[0]
        i=0
        while i<len(s):
            if s[i]!='9':
                min_val=s[i]
                break
            i+=1
        for i in range(len(s)):
            if s[i]==min_val:
                large[i]='9'
        for i in range(len(s)):
            if s[i]==max_val:
                small[i]='0'
        
        large=''.join(large)
        small=''.join(small)
        return int(large)-int(small)
