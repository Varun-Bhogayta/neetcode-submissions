class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ['+','-','*','/']
        
        result = 0
        for token in tokens:
            print(st)
            if token in operators:
                op2 = int(st.pop())
                op1 = int(st.pop())
                result = self.perform_opp(token,op1,op2)
                st.append(result)
                print(st)
            else:
                st.append(token)
        return int(st[-1])

    def perform_opp(self,operator,op1,op2):
        match operator:
            case '+':
                return op1 + op2
            case '-':
                return op1 - op2
            case '*':
                return op1 * op2
            case '/':
                return int(op1 / op2)