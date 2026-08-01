class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i] 
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum2 = nums[left] + nums[right]
                if target == sum2 :
                    result.append([nums[i],nums[right],nums[left]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum2 < target:
                    left += 1    
                else:
                    right -= 1
        return result    

        