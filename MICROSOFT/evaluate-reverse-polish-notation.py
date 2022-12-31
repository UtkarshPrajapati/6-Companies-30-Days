class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if  i not in ["+","-","*","/"]:
                st.append(i)
            else:
                a=int(st.pop())
                b=int(st.pop())
                if i=="+":
                    st.append(b+a)
                if i=="-":
                    st.append(b-a)
                if i=="*":
                    st.append(b*a)
                if i=="/":
                    st.append(b/a)
        return int(st[0])