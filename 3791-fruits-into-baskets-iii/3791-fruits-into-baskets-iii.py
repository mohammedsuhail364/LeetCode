class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        segment_max=[]
        m=len(baskets)
        a=int(sqrt(m))
        k=0
        cnt=0
        mx=0
        for i in range(m):
            if cnt==a:
                segment_max.append(mx)
                mx=baskets[i]
                cnt=1
            else:
                cnt+=1
                mx=max(mx,baskets[i])
        segment_max.append(mx)
        remain=0
        for fruit in fruits:
            k=0
            remain_fruit=1
            for j in range(0,m,a):
                if segment_max[k]<fruit:
                    k+=1
                    continue
                for r in range(j,min(j+a,m)):
                    if baskets[r]>=fruit:
                        baskets[r]=0
                        remain_fruit=0
                        break
                if remain_fruit==0:
                    segment_max[k]=0
                    for r in range(j,min(j+a,m)):
                        segment_max[k]=max(segment_max[k],baskets[r])
                    break
                k+=1
            remain+=remain_fruit
        return remain