class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0 , len(heights) - 1
        max_vol = 0
        while left < right :
            curr_height = min(heights[left],heights[right])
            curr_width = right - left
            curr_vol = curr_height * curr_width
            max_vol = max(max_vol,curr_vol)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_vol
        

        