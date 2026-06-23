class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=set(nums)
        k=len(nums)
        for i in l:
            if nums.count(i)>(k//2):
                return i
    