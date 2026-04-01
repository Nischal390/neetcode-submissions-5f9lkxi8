class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        nump = []
        numn = []
        for num in nums:
            if num>=0:
                nump.append(num)
            else:
                numn.append(num)

        if len(nump) == len(nums):
            numo = [0]*(max(nump)+1)
            for i in nump:
                numo[i]=numo[i]+1
                if numo[i]>1:
                    return True
        #if len(nump)==len(nums):
        #    return False
        elif len(numn) == len(nums):
            numr = [ -x for x in numn]
            nemo = [0]*(max(numr)+1)
            for i in numr:
                nemo[i]=nemo[i]+1
                if nemo[i]>1:
                    return True
        else:
            numr = [ -x for x in numn]
            nemo = [0]*(max(numr)+1)
            for i in numr:
                nemo[i]=nemo[i]+1
                if nemo[i]>1:
                    return True

            numo = [0]*(max(nump)+1)
            for i in nump:
                numo[i]=numo[i]+1
                if numo[i]>1:
                    return True
        return False      