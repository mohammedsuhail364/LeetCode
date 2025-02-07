class Solution:
    def queryResults(self, limit: int, queries):
        colors={}
        color_cnt=defaultdict(int)
        res=[]
        for i,j in queries:
            if i in colors:
                old_color=colors[i]
                color_cnt[old_color]-=1
                if color_cnt[old_color]==0:
                    del color_cnt[old_color]
            colors[i]=j
            color_cnt[j]+=1
            res.append(len(color_cnt))
        return res