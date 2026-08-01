class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        for i in range(n):
            result.append(-1)
            for j in range(i,n):
                if temperatures[i] < temperatures[j]:
                    result[i] = j - i
                    break
            if result[i] == -1:
                result[i] = 0
        
        return result
            
            
        
            
                   
                    