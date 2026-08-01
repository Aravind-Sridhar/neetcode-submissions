class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for idx, val in enumerate(nums):
            complement = target - val

            if complement in res:
                return [res[complement],idx]
            
            res[val] = idx
