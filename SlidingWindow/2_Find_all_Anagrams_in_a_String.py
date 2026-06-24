class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        a=[0]*26
        b=[0]*26
        c=[]
        if len(p)>len(s):
            return []
        for i in range(len(p)):
            a[ord(p[i])-ord("a")]+=1
            b[ord(s[i])-ord("a")]+=1
        if len(p)==len(s):
            if a==b:
                return [0]
            else:
                return []
        for i in range(len(s)-len(p)):
            if a==b:
                c.append(i)
            b[ord(s[i])-ord("a")]-=1
            b[ord(s[i+len(p)])-ord("a")]+=1
        
        if a==b:
            c.append(i+1)
        return c
