class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str

        """
        v=s.split()
        m=" ".join(v[::-1])
        return(m)