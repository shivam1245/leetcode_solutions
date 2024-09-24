class Solution:
    def climbStairs(self, n: int) -> int:
        if (n==1 or n==2 or n==3):
            return n
        

        a = int(3)
        b = int(2)
        while(n-3 > 0):
            a = a + b
            b = a - b
            n -= 1
        return a
        