from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        dic = dic.most_common()
    
        return dic[0][0]
    