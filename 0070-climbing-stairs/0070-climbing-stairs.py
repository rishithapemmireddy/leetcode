class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        for i in range(n):
            temp=a+b
            a=b
            b=temp
        return b