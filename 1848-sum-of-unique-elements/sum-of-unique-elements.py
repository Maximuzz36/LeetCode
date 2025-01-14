class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        v=set()
        dv=set()

        for i in nums:
            if i not in v and i not in dv:
                v.add(i)
            else:
                if i in v:
                    v.remove(i)
                dv.add(i)
        return sum(v)

        