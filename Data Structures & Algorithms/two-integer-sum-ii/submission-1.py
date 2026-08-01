class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left<right:
            diff = target - numbers[left] - numbers[right]
            if diff > 0:
                left += 1
            elif diff < 0:
                right -= 1
            else:
                return [left+1,right+1]
            
        