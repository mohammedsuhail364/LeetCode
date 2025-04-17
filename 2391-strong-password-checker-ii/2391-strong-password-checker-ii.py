class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        lower=False
        upper=False
        digit=False
        special=False
        prev=-1
        for i in range(len(password)):
            if 'A'<=password[i]<='Z':
                upper=True
            if 'a'<=password[i]<='z' :
                lower=True
            if password[i] in '1234567890':
                digit=True
            if password[i] in '!@#$%^&*()-+':
                special=True
            if i==0:
                prev=password[i]
                continue
            if prev==password[i]:
                return False
            prev=password[i]
        return lower and upper and digit and special