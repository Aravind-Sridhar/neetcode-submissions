class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r = 0,len(nums)-1

        while l<=r:
            if nums[l]==val:
                if nums[r]!=val:
                    nums[l],nums[r] = nums[r],nums[l]
                    l+=1
                    r-=1
                else:
                    r-=1
            else:
                l+=1
        
        return l