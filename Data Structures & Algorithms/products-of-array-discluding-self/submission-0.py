class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        
        for index,num in enumerate(nums):
            for index_res in range(len(nums)):
                if index_res == index:
                    continue
                result[index_res] *= num
        
        return result
