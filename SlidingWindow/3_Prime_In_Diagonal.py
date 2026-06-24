class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        c=0

        if len(nums)>300:
            return 0
        if len(nums)!=len(nums[0]):
            return 0
        for i in range(len(nums)):
            x=nums[i][i]
            if x>1:
                p=True
                for j in range(2,int(x**0.5)+1):
                    if nums[i][i]%j==0:
                        p=False
                        break
                if p:
                    c=max(c,x)

            y=nums[i][len(nums)-i-1]
            if y>1:
                p=True

                for k in range(2,int(y**0.5)+1):
                    if nums[i][len(nums)-i-1]%k==0:
                        p=False
                        break
                if p:
                    c=max(c,y)
            
        return c
