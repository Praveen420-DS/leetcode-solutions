class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        k=str(x)
        if k==k[::-1]:
            return True
        else :
            return False