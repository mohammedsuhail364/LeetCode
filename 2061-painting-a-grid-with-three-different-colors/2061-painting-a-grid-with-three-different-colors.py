# refer techdose youtube channel
class Solution:
    MOD=10**9+7
    def __init__(self):
        self.state_mem=[[-1]*1024 for i in range(1002)]
    def countWays(self,m,n,r,c,curr_state,prev_state):
        if c==n:
            return 1
        if r==m:
            return self.countWays(m,n,0,c+1,0,curr_state)
        if r==0 and self.state_mem[c][prev_state]!=-1:
            return self.state_mem[c][prev_state]
        up_color=0
        if r>0:
            up_color=curr_state&3
        left_color=(prev_state>>((m-r-1)*2))&3
        ways_color=0
        for color in range(1,4):
            if (color != up_color and color != left_color):
                new_state=(curr_state<<2)|color
                ways_color=(ways_color+self.countWays(m,n,r+1,c,new_state,prev_state))%self.MOD
        if r==0:
            self.state_mem[c][prev_state]=ways_color
        return ways_color

    def colorTheGrid(self, m: int, n: int) -> int:
        return self.countWays(m,n,0,0,0,0)
        