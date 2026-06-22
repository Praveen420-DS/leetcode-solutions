# LeetCode 1 - Two Sum
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        
        l={}
        for i in range(len(nums)):
            c=nums[i]
            k=target-c
            if k in l:
               return [l[k],i]
            l[c]=i 

        return []   
        