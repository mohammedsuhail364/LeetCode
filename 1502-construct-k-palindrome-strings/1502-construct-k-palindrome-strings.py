class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        count=Counter(s)
        odd=0
        for i,j in count.items():
            if j%2!=0:
                odd+=1
        if odd>k:
            return False
        return True

