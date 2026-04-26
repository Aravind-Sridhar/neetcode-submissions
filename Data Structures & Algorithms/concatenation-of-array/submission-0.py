class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [x for x in nums]
        ans.extend(x for x in nums)
        return ans