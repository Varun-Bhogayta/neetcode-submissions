class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq_len = 0
        for num in num_set:
           if num-1 not in num_set:

            current_len = 1
            current_num = num
            while num+1 in num_set:
                current_len += 1
                num += 1
            
            max_seq_len = max(max_seq_len,current_len)
        return max_seq_len