class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        par = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in par.values():
                stk.append(char)
                print("push")
            elif stk != [] and par[char] == stk[-1]:
                stk.pop()
                print("pop")
            else:
                return False
        return stk == []
                

