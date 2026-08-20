class Solution:
    def isValid(self, s: str) -> bool:
        def verify(x,y):
            if x == "{" and y=="}":return True
            elif x == "[" and y=="]":return True
            elif x == "(" and y==")":return True
            else: return False
        st = []
        for p in s:
            if p in "({[": st.append(p)
            elif st and verify(st.pop(),p):continue
            else: return False
        
        return True if not st else False

        