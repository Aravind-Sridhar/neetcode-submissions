class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dic = {}

        for _, val in enumerate(nums):
            if val not in dic:
                dic[val] = 1
            else:

                dic[val] +=1

        print(dic)

        for x in dic.values():
            print(x)
            if x != 1:
                return True

        return False
         