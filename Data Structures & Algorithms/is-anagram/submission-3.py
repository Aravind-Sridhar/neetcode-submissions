class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1= {}
        d2 = {}
        
        for _, val in enumerate(s):
            if val not in d1:
                d1[val] = 1
            else:
                d1[val]+=1
        

        for _, val in enumerate(t):
            if val not in d2:
                d2[val] = 1
            else:
                d2[val]+=1

        return d1==d2
        