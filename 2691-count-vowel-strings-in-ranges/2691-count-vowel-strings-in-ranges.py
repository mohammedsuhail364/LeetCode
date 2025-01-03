class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum=[0]*len(words)
        res=[]
        for i,w in enumerate(words):
            if i==0:
                if w[0] in 'aeiou' and w[-1] in 'aeiou':
                    prefix_sum[i]+=1
            else:
                if w[0] in 'aeiou' and w[-1] in 'aeiou':
                    prefix_sum[i]=prefix_sum[i-1]+1
                else:
                    prefix_sum[i]=prefix_sum[i-1]
        # print(prefix_sum)
        for i,j in queries:
            if i==0:
                res.append(prefix_sum[j])
            else:
                res.append(prefix_sum[j]-prefix_sum[i-1])
        return res
