class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2)<len(s1):
            return False
        k=len(s1)
        c=[0]*26
        d=[0]*26
        for i in range(k):
            c[ord(s1[i])-ord("a")]+=1
            d[ord(s2[i])-ord("a")]+=1
            
        for i in range(len(s2)-k):
            if c==d:
                return True
            
            d[(ord(s2[i]))-ord("a")]-=1
            d[(ord(s2[i+k]))-ord("a")]+=1
        return c==d
                
            
           

