class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start, end = 1, max(piles)
        res = end

        while start <= end:
            mid = start + (end - start) // 2
            print(mid,start,end)            
            total_hours = sum(math.ceil(p / mid) for p in piles)
            
            if total_hours <= h:
                res = mid
                end = mid - 1
            else:
                start = mid + 1

        return res