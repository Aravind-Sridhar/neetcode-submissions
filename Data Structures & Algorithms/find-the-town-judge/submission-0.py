class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n+1)
        trusted_by = [0] * (n+1)

        for val in trust:
            a,b = val

            trusts[a]+=1
            trusted_by[b]+=1
        
        for i in range(len(trusts)):
            if trusts[i] == 0 and trusted_by[i] == n-1:
                return i
        
        return -1
