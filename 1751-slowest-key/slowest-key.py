class Solution:
    def slowestKey(self, releaseTimes: List[int], keys: str) -> str:

        pre=0
        maxk=0
        mc=''
        for i in range(len(releaseTimes)):
            m=releaseTimes[i]-pre
            if maxk<=m:
                mc=keys[i] if maxk!=m or (maxk==m and ord(keys[i])>ord(mc)) else mc
                maxk=m 
            pre =releaseTimes[i]
        return mc
        
        