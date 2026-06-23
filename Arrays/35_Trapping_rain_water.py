class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        left=0
        right=0
        w=0
        while(l<r):
            if height[l]<height[r]:
                if height[l]>=left:
                    left=height[l]
                else:
                    w+=left-height[l]
                l+=1
            else:
                if height[r]>=right:
                    right=height[r]
                else:
                    w+=right-height[r]
                r-=1
            
        return w