class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index,height in enumerate(heights):
            start = index
            
            while stack and stack[-1][1] > height:
                st_index, st_height = stack.pop()
                max_area = max(max_area, st_height * (index - st_index))
                start = st_index
                
            stack.append((start, height))

        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area
