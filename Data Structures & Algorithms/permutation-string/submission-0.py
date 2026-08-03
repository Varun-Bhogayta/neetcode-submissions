class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mp = {}
        for char in s1:
            mp[char] = mp.get(char, 0) + 1

        len_1 = len(s1)
        left = 0

        for right in range(len(s2)):
            if s2[right] in mp:
                mp[s2[right]] -= 1
                while mp[s2[right]] < 0:
                    if s2[left] in mp:
                        mp[s2[left]] += 1
                    left += 1
                if right - left + 1 == len_1:
                    return True
            else:
                while left < right:
                    if s2[left] in mp:
                        mp[s2[left]] += 1
                    left += 1
                left = right + 1

        return False