class Solution:
    def racecar(self, target: int) -> int:
        # refer this https://www.youtube.com/watch?v=DBJPWJr5zZ4
        q=deque([(0,0,1)]) # position,moves,speed
        visit=set()
        while q:
            position,moves,speed=q.popleft()
            if position ==target:
                return moves
            if (position,speed) in visit:
                continue
            visit.add((position,speed))
            q.append((position+speed,moves+1,speed*2))
            if(position+speed>target and speed>0) or (position+speed<target and speed<0):
                speed=-1 if speed >0 else 1
                q.append((position,moves+1,speed))