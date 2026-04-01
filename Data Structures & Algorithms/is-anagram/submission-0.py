class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            this={}
            that={}

            for i in s:
                if i in this:
                    this[i]=this[i]+1
                else:
                    this[i]=1

            for j in t:
                if j in that:
                    that[j]=that[j]+1
                else:
                    that[j]=1


            if this == that:
                return True
            else:
                return False
        else:
            return False   