class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t=sorted(nums)
        k=[]
        print(t)
        for i in nums:
            # print(t.index(i))
            k.append(t.index(i))
        return k