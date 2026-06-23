class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,m=0,len(height)-1,0
        while(i<j):
            w=j-i
            area=min(height[i],height[j])*w
            m=max(m,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return m