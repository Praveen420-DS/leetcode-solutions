class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        l=[0]*len(s)
        a=0
        m=0
        for i in range(len(s)):
            if c==s[i]:
                m=i
                break
        for i in range(m,len(s)):
            if c==s[i]:
                l[i]=a
                a=0
            else:
                a+=1
                l[i]=a
        for i in range(len(s)-1,m,-1):
            if c==s[i]:
                a=0
                l[i]=a
            else:
                a+=1
                l[i]=min(a,l[i])
        a=1
        for i in range(m-1,-1,-1):
            
            l[i]=a
            a+=1

        return l

           