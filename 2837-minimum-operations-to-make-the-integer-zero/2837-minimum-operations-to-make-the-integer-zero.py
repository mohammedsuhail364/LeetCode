class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # num1=num1−(2^i+num2)
        # num1=num1−((2^i1​+num2)+(2^i2​+num2)+...+(2^ik​+num2))
        # num1=num1−(k⋅num2+(2^i1​+2^i2​+...+2^ik​))
        # 0=num1−(k⋅num2+∑2^i​)
        # => num1-k.num2-(2^i1​+2^i2​+...+2^ik​)
        # then => (2^i1​+2^i2​+...+2^ik​) = num1-k.num2
        # so we want to find k and return it condition => x >= 0 and count of 1 in x <=k<=x
        for k in range(61):
            x=num1-(k*num2)
            if x<0:
                continue
            one_count=bin(x).count('1')
            if one_count<=k<=x:
                return k
        return -1