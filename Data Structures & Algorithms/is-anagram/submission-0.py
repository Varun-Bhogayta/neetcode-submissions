class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = self.sort_str(s)
        t_sorted = self.sort_str(t)
        return s_sorted == t_sorted
    
    @staticmethod
    def sort_str(s :str) -> str:
        return "".join(sorted(s))