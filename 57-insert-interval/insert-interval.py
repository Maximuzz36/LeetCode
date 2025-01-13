class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        t=[]
        def is_overlapping(interval1, interval2):
            a1, b1 = interval1
            a2, b2 = interval2
            return max(a1, a2) <= min(b1, b2)
        for i in intervals:
            if is_overlapping(newInterval,i):
                t.extend(i)
        t.extend(newInterval)
        st,end=min(t),max(t)
        k=[]
        for i in intervals:
            if not is_overlapping([st,end],i):
                k.append(i)
        k.append([st,end])
        k=sorted(k,key=lambda x:x[0])
        return k
        