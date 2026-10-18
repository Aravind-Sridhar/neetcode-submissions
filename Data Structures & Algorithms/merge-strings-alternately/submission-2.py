class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l,r=0,0
        l1,l2 = len(word1), len(word2)
        while l < l1 or r < l2:

            if l < l1:
                res+=word1[l]
                l+=1
            if r < l2:
                res+=word2[r]
                r+=1

        return res
        