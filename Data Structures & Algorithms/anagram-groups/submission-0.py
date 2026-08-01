class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        strs_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in strs_map:
                strs_map[sorted_word].append(word)
            else:
                strs_map[sorted_word] = [word]
        
        for value_list in strs_map.values():
            result.append(value_list)
        
        return result
            
