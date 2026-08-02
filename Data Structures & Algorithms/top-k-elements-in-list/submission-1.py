## Using Bucket sort
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in dic.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket)-1, 0,-1): # tranversing from last
            for num in bucket[i]: # getting the element from corresponding bucket
                result.append(num)
            
            if len(result) == k:
                return result
        