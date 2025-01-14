class Solution:
    def reformatNumber(self, number: str) -> str:
        
        number=number.replace(" ","")
        number=number.replace("-","")
        n=len(number)
        print(number)
        i=0
        t=''
        print("len: ",n)
        while i<n:
            print(t,i)
            print('-->',n-i)
            if n-i==4:
                t+=number[i:i+2]+"-"+number[i+2:]+"-"
                break
            else:
                t+=number[i:i+3]+"-"
                i+=3
        return t[:len(t)-1]





        