class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num,freq in nums_map.items():
            bucket[freq].append(num)
        
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if k < 1:
                    return res
        
        
        