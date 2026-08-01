class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left , right = 0 , len(heights) - 1
        max_vol = 0
        # while left < right :
        #     curr_height = min(heights[left],heights[right])
        #     curr_width = right - left
        #     curr_vol = curr_height * curr_width
        #     max_vol = max(max_vol,curr_vol)
        # return max_vol
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                curr_height = min(heights[i],heights[j])
                curr_width = j - i 
                curr_vol = curr_height * curr_width
                max_vol = max(max_vol,curr_vol)
        return max_vol

        