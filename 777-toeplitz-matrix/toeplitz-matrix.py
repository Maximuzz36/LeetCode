class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        t={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in t:
                    if t[i-j]!=matrix[i][j]:
                        return False
                else:
                    t[i-j]=matrix[i][j]
        return True


        