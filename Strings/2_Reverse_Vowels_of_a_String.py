class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p="AEIOUaeiou"
        s=list(s)
        i=0
        j=len(s)-1
        while(i<=j):
            if s[i]in p and s[j] in p:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in p:
                i+=1
            elif s[j] not in p:
                j-=1
        return "".join(s)