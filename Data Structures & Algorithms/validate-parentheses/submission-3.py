class Solution:
    def isValid(self, s: str) -> bool:
        has = {')': '(', ']': '[', '}': '{'}
        st = []

        for i in s:
            if i in has:
                if st and st[-1] == has[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)

        if not st:
            return True
        else:
            return False