class Solution:
    def maxDiff(self, num: int) -> int:
        s=list(str(num))
        max_val=list(str(num))
        min_val=list(str(num))
        min_v=0
        max_v=0
        flag=False
        for i in range(len(s)):
            if s[i]!='1' and s[i]!='0':
                min_v=s[i]
                flag=True if i==0 else False
                break
        for i in range(len(s)):
            if s[i]!='9':
                max_v=s[i]
                break
        for i in range(len(s)):
            if s[i]==min_v and not flag:
                min_val[i]='0'
            elif s[i]==min_v and flag:
                min_val[i]='1'
        for i in range(len(s)):
            if s[i]==max_v:
                max_val[i]='9'
        max_val=''.join(max_val)
        min_val=''.join(min_val)
        return int(max_val)-int(min_val)

        
        