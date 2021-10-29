class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for i in range(x+1,len(nums)):
                if nums[x]+nums[i]==target:
                    return [x,i]
