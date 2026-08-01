class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}
        for index,num in enumerate(numbers):
            diff = target - num
            if diff in num_map:
                return [num_map[diff]+1,index+1]
            num_map[num] = index

            
            
        