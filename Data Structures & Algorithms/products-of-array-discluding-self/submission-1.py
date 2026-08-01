class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        prefix_prod = 1
        suffix_prod = 1

        for i in range(len(nums)):
            result[i] *= prefix_prod
            prefix_prod *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix_prod
            suffix_prod *= nums[i]
        
        return result
