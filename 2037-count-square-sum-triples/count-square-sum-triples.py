class Solution:
    def countTriples(self, n: int) -> int:
        k=pow(n,2)
        t=set()
        for i in range(1,n):
            for j in range(i+1,n):
                tm=pow(pow(i,2)+pow(j,2),0.5)
                if tm<=n and int(tm)==tm:
                    t.add((i,j))
        # print(t)
        return len(t)*2




        