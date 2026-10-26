class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_clean = bin(n)[2:]

        count = 0
        for x in binary_clean:
            if x =='1':
                count+=1

        return count 