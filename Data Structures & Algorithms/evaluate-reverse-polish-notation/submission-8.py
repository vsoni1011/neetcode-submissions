class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(x,y,o):
            if o=="+":return x+y
            elif o=="*":return x*y
            elif o == "-":return y-x
            else: return int(y/x)
        
        st = []
        for i in tokens:
            if i in "+-*/":
                st.append(operation(st.pop(),st.pop(),i))
            else:
                st.append(int(i))
        return st[-1]
        