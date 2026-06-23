class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        c=prices[0]
     
        v=0
        for i in range(1,len(prices)):
            if prices[i]<c:
                c=prices[i]
                continue
            v=max(v,prices[i]-c)
        return v
        