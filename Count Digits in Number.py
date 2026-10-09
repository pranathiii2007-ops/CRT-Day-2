class Solution:
    def countDigits(self, n: int) -> int:
        if n==0:
            return 1
        c=0
        while n!=0:
            n=n//10
            c+=1
        return c
            