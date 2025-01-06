class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)
        box=0
        moves=0
        for i in range(len(boxes)):
            res[i]+=box+moves
            moves=box+moves
            if boxes[i]=='1':
                box+=1
        box=0
        moves=0
        for i in reversed(range(len(boxes))):
            res[i]+=box+moves
            moves=box+moves
            if boxes[i]=='1':
                box+=1
        return res