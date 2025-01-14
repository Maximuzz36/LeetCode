class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i,j=0,0
        ct=0
        while i<len(g) and j<len(s) :

            if g[i]<=s[j]:
                i+=1
                ct+=1
            j+=1

        return ct
            

        