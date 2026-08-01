class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seq_len = 1
        max_seq_len = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                seq_len += 1
            elif nums[i] == nums[i+1]:
                pass
            else:
                max_seq_len = max(max_seq_len,seq_len)
                seq_len = 1 
        max_seq_len = max(max_seq_len,seq_len)
        return max_seq_len