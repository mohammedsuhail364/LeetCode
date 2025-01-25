from collections import deque
# refer neetcode
class Solution:
    def lexicographicallySmallestArray(self, nums, limit: int):
        new_nums=sorted(nums)
        res=[0]*len(nums)
        q=[]
        q_map={}
        v=0
        for i in range(len(nums)):
            if i==0:
                q.append(deque())
                q[v].append(new_nums[i])
                
            elif 0<=new_nums[i]-new_nums[i-1]<=limit:
                q[v].append(new_nums[i])
            else:
                q.append(deque())
                v+=1
                q[v].append(new_nums[i])
            q_map[new_nums[i]]=v
        for i in range(len(nums)):
            index=q_map[nums[i]]
            res[i]=q[index].popleft()
        return res
                