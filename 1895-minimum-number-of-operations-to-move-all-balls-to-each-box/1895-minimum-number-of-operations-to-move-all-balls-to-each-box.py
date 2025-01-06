class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)
        for i in range(len(boxes)):
            temp=0
            x=0
            while x < len(boxes):
                if x==i:
                    x+=1
                    continue
                if boxes[x]=="1":
                    temp+=abs(i-x)
                x+=1
            res[i]=temp
        return res

            