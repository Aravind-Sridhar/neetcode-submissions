## Using Bucket sort
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        result = []
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in dic.items():
            bucket[freq].append(num)

        for i in range(len(bucket)-1, 0,-1): # tranversing from last
            for num in bucket[i]: #
                result.append(num)
            
            if len(result) == k:
                return result
        