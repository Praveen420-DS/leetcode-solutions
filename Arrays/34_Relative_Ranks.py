class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
    
        # Sort scores in descending order
        sorted_scores = sorted(score, reverse=True)

        # Store rank of each score
        rank = {}

        for i in range(len(sorted_scores)):
            if i == 0:
                rank[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                rank[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                rank[sorted_scores[i]] = "Bronze Medal"
            else:
                rank[sorted_scores[i]] = str(i + 1)

        # Build the answer in original order
        ans = []
        for s in score:
            ans.append(rank[s])

        return ans