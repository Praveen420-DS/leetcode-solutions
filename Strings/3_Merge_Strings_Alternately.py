class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        r=""
        while(i<len(word1) and j<len(word2)):
            r+=word1[i]
            r+=word2[j]
            i+=1
            j+=1
        if len(word1)<len(word2):
            while(j<len(word2)):
                r+=word2[j]
                j+=1
        elif len(word1)>len(word2):
            while(i<len(word1)):
                r+=word1[i]
                i+=1
        return r