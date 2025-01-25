from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        t=[i for i in licensePlate.lower() if i.isalpha()]
        t=t
        l=None
        counter1 = Counter(t)
        for i in words:
            print(t,sorted(list(i.lower())))
            counter2 = Counter(list(i.lower()))
            if all(counter1[key] <= counter2[key] for key in counter1):
                if l==None or len(l)>len(i):
                    l=i

        return l
        