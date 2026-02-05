class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 2 2 2 2 2
        #     3 3 3 3 3
        diff=[0]*1000
        for inc,s,e in trips:
            diff[s]+=inc
            if e<len(diff):
                diff[e]-=inc
        cur_seat=0
        for n in diff:
            cur_seat+=n
            if cur_seat>capacity:
                return False
        return True
        # [0,0,0,0,0,0,0] 
        # +2         -2 
        #                    