class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       

        l=[x*x for x in nums]
        l.sort()
        return l
