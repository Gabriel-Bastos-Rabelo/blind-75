class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)//2):
            last = matrix[i][i]
            for j in range(len(matrix)-i-i-1):

                #up row
                for k in range(i, len(matrix) - i):
                    matrix[i][k], last = last, matrix[i][k]
                print(matrix)
                print(last)

                #right col
                for k in range(i + 1, len(matrix)-i):
                    matrix[k][len(matrix)-i-1], last = last, matrix[k][len(matrix)-i-1]

                print(matrix)

                
                for k in range(len(matrix)-i-2, i-1, -1):
                    matrix[len(matrix)-i-1][k], last = last, matrix[len(matrix)-i-1][k]

                print(matrix)

                #left row

                for k in range(len(matrix)-i-2, i-1, -1):
                    matrix[k][i], last = last, matrix[k][i]

                print(matrix)


                


                

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #The approach here to solve this problem is first reverse the matrix and then is necessary to swap the symmetry of the matrix, and this will result in the matrix rotate
        for i in range(len(matrix)//2):
            for j in range(len(matrix)):
                matrix[i][j], matrix[len(matrix)-i-1][j] = matrix[len(matrix)-i-1][j], matrix[i][j]


        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        

                


                

        