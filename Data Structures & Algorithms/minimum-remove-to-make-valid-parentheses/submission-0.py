class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        remove_set = set()
        out = ""
        for idx,ch in enumerate(s):
            if ch not in ['(', ')']:
                continue
            if ch == "(":
                st.append(idx)
            else:
                if len(st)==0:
                    remove_set.add(idx)
                else:
                    st.pop()
        if len(st)>0:
            for idx in st:
                remove_set.add(idx)
        for idx,ch in enumerate(s):
            if idx not in remove_set:
                out+=ch

        return out