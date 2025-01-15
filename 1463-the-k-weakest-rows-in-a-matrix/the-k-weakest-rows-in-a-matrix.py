class Solution:
    def kWeakestRows(self, mat: List[List[int]], np: int) -> List[int]:
        t=[]
        for i,j in enumerate(mat):
            print(i,j)
            t.append((i,sum(j)))
        t=sorted(t, key=lambda x:(x[1], x[0]),reverse=True)
        t=t[::-1]
        k=[]
        for i in range(np):
            k.append(t[i][0])
        return k



        