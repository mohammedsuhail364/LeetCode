from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c=Counter(word)
        li=[i for i in c.values()]
        li.sort()
        n=len(li)
        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+li[i]
        res=inf
        for i in range(n):
            # we can make the k special array starts from i index then we want to remove 
            # some elements before i that tells the prefix sum array
            deletions=prefix_sum[i]
            for j in range(i+1,n):
                if li[j]>li[i]+k:
                    deletions += li[j]-li[i]-k
            res=min(res,deletions)
        return res