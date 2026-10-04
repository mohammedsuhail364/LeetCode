class Solution:
    def checkValidString(self, s: str) -> bool:
        left =[]
        star = []
        for idx,i in enumerate(s):
            if i =="(":
                left.append(idx)
            elif i =="*":
                star.append(idx)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star and left[-1]<star[-1]:
            left.pop()
            star.pop()
        if left:
            return False
        return True