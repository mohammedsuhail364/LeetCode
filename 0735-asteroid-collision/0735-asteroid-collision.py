class Solution:
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids:
            if i>0:
                stack.append(i)
                continue
            while stack and stack[-1]>0:
                if not stack:
                    stack.append(i)
                    break
                tmp=stack.pop()
                if abs(i)<tmp:
                    stack.append(tmp)
                    break
                elif abs(i)==tmp:
                    break 
            
        return stack