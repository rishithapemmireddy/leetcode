class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min,max= -2**31,2**31-1
        a=str(x)
        if x<0:
            a=a[1:]
            a="-"+a[::-1]
            rev=int(a)
        else:
            a=a[::-1]
            rev=int(a)
        if rev>max or rev<min:
            return 0
        return rev