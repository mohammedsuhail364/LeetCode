class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        temp=[]
        for li in matrix:
            if temp:
                tmp=list(map(int,li))
                tmp1=temp[-1]
                for i in range(len(tmp)):
                    if tmp[i]:
                        tmp[i]=tmp1[i]+tmp[i]
                temp.append(tmp)
            else:
                temp.append(list(map(int,li)))
        def findNSE(nums):
            stack=[]
            nse=[len(nums)]*len(nums)
            for i in range(len(nums)):
                while stack and nums[stack[-1]]>nums[i]:
                    idx=stack.pop()
                    nse[idx]=i
                stack.append(i)
            return nse
        def findPSEE(nums):
            stack=[]
            pse=[-1]*len(nums)
            for i in range(len(nums)):
                while stack and nums[stack[-1]]>nums[i]:
                    stack.pop()
                if stack:
                    pse[i]=stack[-1]
                stack.append(i)
            return pse
        res=0
        for li in temp:
            nse=findNSE(li)
            pse=findPSEE(li)
            for i in range(len(li)):
                width=nse[i]-pse[i]-1
                height=li[i]
                res=max(res,width*height)
        return res

[["0","1"],
 ["1","0"]]