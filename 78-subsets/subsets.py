class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        t=[]
        def recur(st,subs):
            t.append(subs[:])
            print(subs)
            for i in range(st,len(nums)):
                subs.append(nums[i])
                recur(i+1,subs)
                subs.pop()
        recur(0,[])
        return t



        