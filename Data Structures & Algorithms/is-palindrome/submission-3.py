class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0,len(s)-1
        s = s.lower()
        while left < right:
            if not s[left].isalnum():
                print("removed at ",left)
                left += 1
                continue

            if not s[right].isalnum():
                print("removed at ",right)
                right -= 1
                continue

            if s[left] == s[right]:
                print("is equal",left," ",right)
                left += 1
                right -= 1
            else:
                print("is not equal",left," ",right)
                return False
        return True 