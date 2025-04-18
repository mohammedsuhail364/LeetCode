class Solution:
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids:
            if i>0 :
                
                stack.append(i)
            elif i<0 :
                
                while stack and stack[-1]>0:
                    if not stack:
                        stack.append(i)
                        break
                    val=stack.pop()
                    if val>abs(i):
                        stack.append(val)
                        break
                    elif val==abs(i):
                        break
                else:
                    stack.append(i)
        return stack