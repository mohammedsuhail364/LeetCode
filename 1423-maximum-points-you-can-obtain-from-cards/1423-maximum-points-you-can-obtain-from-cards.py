class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        n=len(cardPoints)
        cur_sum=0
        l=0
        window=n-k
        res=0
        for r in range(len(cardPoints)):
            cur_sum+=cardPoints[r]
            while (r-l+1)>window:
                cur_sum-=cardPoints[l]
                l+=1
            if (r-l+1)==window:
                temp=total-cur_sum
                res=max(res,temp)
        return res

            
