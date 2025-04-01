class Solution:
    def mostPoints(self, questions) -> int:
        cache=[0]*len(questions)
        def backtrack(i):
            if i>=len(questions):
                return 0
            if cache[i]:
                return cache[i]
            points,brainpower=questions[i]
            cache[i]= max(backtrack(i+1),points+backtrack(i+brainpower+1))
            return cache[i]
        return backtrack(0)
         