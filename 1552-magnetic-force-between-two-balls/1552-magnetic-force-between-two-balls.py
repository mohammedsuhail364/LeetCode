class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlaceBalls(g):
            last=position[0] # always start at 0 th position
            count=1 # always place the ball in 0 th position
            for i in range(1,len(position)):
                if position[i]-last>=guess: # we can place a ball
                    count+=1
                    last=position[i]
                    if count==m:
                        return True
            return False
        position.sort() # important one then only we can easily find the distance
        # core concept of koko eating banana
        # we can guess the minimum number and check if this is the minimum we can place 'm' balls if yes we can set the ans and check the higher values
        l=1 # because all element are distinct so 0 cannot minimum
        r=position[-1]-position[0]
        while l<=r:
            guess=(l+r)//2
            if canPlaceBalls(guess):
                res=guess
                l=guess+1 # try to maximize the values
            else:
                r=guess-1 # we cannot place m balls so we can reduce the guess value
        return res