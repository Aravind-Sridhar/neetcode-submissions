from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        match = next((k for k, v in dic.items() if v ==1), None)
        return match