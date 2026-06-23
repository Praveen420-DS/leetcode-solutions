class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a=[]
        b=[]
        c=[]
        for i in range(n):
            a.append(nums[i])
        for i in range(n,len(nums)):
            b.append(nums[i])
        for i in range(n):
            c.append(a[i])
            c.append(b[i])
        return c