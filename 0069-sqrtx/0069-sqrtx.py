class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        l,r=0,x
        while l<=r:
            m=(l+r)//2
            if m*m == x:
                return m
            elif m*m < x:
                l = m+1
                res=m
            else:
                r=m-1
        return res
            
        