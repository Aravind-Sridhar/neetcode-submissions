class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(x) for x in digits])
        plus = 1+int(num)
        res=[]
        for x in str(plus):
            res.append(int(x))
        return res