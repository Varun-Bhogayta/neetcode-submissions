class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        st = []
  
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                st_i = st.pop()
                result[st_i] = i - st_i
            st.append(i)
    
        return result
            
            
        
            
                   
                    