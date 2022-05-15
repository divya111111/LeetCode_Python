class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b=0
        s=1
        maxi=0
        while(s<len(prices)):
            if( prices[s] > prices[b] ):
                diff=prices[s]-prices[b]
                maxi=max(maxi,diff)
            else:
                b=s
            s=s+1
                            
        
        return maxi