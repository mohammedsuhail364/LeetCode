from collections import defaultdict,Counter
class Solution:
    def wordSubsets(self, words1, words2):
        store=[]
        for i in words1:
            temp=defaultdict(int)
            for x in i:
                temp[x]+=1
            store.append(temp)
        
        res=[]
        words2_new=defaultdict(int)
        for index,i in enumerate(words2):
            temp=defaultdict(int)
            for x in i:
                temp[x]+=1
            if index==0:
                words2_new=temp
                continue
            for x in temp:
                words2_new[x]=max(words2_new[x],temp[x])
            
        for i,x in enumerate(store):
            flag=True
            for y in words2_new:
                if y not in words2_new or words2_new[y]>x[y]:
                    flag=False
            if flag:
                res.append(words1[i])
        return res