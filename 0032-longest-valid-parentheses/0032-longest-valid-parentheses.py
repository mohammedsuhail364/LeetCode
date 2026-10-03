class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=0
        # this question basically upgrade of the valid parenthesis but in this we can go through two pass why because of 
        left , right =0,0
        for i in s:
            if i==")":right+=1
            elif i=="(":left+=1
            if left==right:
                res=max(res,2*left)
            if right > left :
                left , right =0,0
                # in this case we dont get any valid parenthesis at this string 
                # start with fresh
        # this only not enough because this doesnt capture this Left → Right misses "(()"
        # but it is not valid and also not a valid right so we cannot capture this but in the opposite traversal we can capture this 
        left , right =0,0
        for i in s[::-1]:
            if i==")":right+=1
            elif i=="(":left+=1
            if left==right:
                res=max(res,2*left)
            if left > right :
                left , right =0,0
        return res