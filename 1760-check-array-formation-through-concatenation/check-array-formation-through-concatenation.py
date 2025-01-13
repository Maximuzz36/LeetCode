class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        k=[]
        for i in pieces:
            t=str(i)
            print(arr,t[1:len(t)-1])
            if t[1:len(t)-1] not in str(arr):
                return False
            k.extend(i)
        k.sort()
        arr.sort()
        if k==arr:
            return True
        return False
        
        