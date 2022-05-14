class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=3
        if (n==3) or (n==1):
            return True
      
        while(a<n):
            a=a*3
        if (a==n):
            return True
        else:
            return False
        return False