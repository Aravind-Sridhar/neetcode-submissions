class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for x in operations:
            if x == '+':
                res.append(int(res[-1])+ int(res[-2]))
            elif x == 'D':
                res.append(2*int(res[-1]))
            elif x == 'C':
                res.pop()
            else:
                res.append(int(x))
        
        return int(sum(res))