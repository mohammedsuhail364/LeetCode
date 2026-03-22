class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={v:i for i,v in enumerate(s)}
        start=0
        max_index=0
        res=[]
        for i in range(len(s)):
            max_index=max(max_index,last_index[s[i]])
            if i==max_index:
                res.append(i-start+1)
                start=i+1
        return res