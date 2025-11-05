from sortedcontainers import SortedList
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # refer neetcode
        top=SortedList()
        remain=SortedList()
        freq=defaultdict(int)
        cur_sum=0
        res=[]
        def balance():
            nonlocal cur_sum
            if len(top)>x:
                f,n=top.pop(0)
                cur_sum-=(f*n)
                remain.add((f,n))
            if len(top)<x and remain:
                f,n=remain.pop()
                top.add((f,n))
                cur_sum+=(f*n)
            if top and remain and top[0]<remain[-1]:
                f1,n1=top.pop(0)
                f2,n2=remain.pop()
                cur_sum-=(f1*n1)
                top.add((f2,n2))
                remain.add((f1,n1))
                cur_sum+=(f2*n2)
        def add(num):
            nonlocal cur_sum
            if num in freq:
                prev=(freq[num],num)
                if prev in top:
                    top.remove(prev)
                    cur_sum-=(freq[num]*num)
                elif prev in remain:
                    remain.remove(prev)
            freq[num]+=1
            top.add((freq[num],num))
            cur_sum+=(freq[num]*num)
            balance()
        def remove(num):
            nonlocal cur_sum
            if num in freq:
                prev=(freq[num],num)
                if prev in top:
                    top.remove(prev)
                    cur_sum-=(freq[num]*num)
                elif prev in remain:
                    remain.remove(prev)
            freq[num]-=1
            if freq[num]==0:
                del freq[num]
            else:
                top.add((freq[num],num))
                cur_sum+=(freq[num]*num)
            balance()

        for i in range(k):
            add(nums[i])
        res.append(cur_sum)
        for i in range(k,len(nums)):
            remove(nums[i-k])
            add(nums[i])
            res.append(cur_sum)
        return res
        