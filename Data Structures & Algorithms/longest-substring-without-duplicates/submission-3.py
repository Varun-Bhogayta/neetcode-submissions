class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        ss = ""
        for char in s:
            if char in ss:
                print(ss,len(ss))
                result = max(result,len(ss))
                ss = ss[ss.find(char)+1:] + char
            else:
                ss += char
        result = max(result,len(ss))
        return result
            

        