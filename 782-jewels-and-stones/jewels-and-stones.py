class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        t=0
        for i in stones:
            if i in jewels:
                t+=1
        return t
        