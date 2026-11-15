from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        res = []

        sort = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        for key in sort.keys():
            res.append(key)
        
        return res[:k]