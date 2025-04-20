class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s.count('e') + s.count('E') > 1:
            return False
        if s in['inf','-inf','nan',"+inf","Infinity","-Infinity","+Infinity"]:
            return False
        try:
            float(s)
            return True
        except ValueError:
            return False
        

        
        