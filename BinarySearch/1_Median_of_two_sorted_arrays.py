class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1=sorted(nums1+nums2)
        mid=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[mid]
        else:
            v=(nums1[mid]+nums1[mid-1])/2.0
            return v


            
