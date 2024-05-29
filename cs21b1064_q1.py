
import numpy as np
def printmatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
        print()
            

def matrix_addition(mat1, mat2):
    return np.add(mat1, mat2)
def matrix_subtraction(mat1, mat2):
    return np.subtract(mat1, mat2)
def scalar_matrix_multiplication(mat1, scalar):
    return np.multiply(mat1, scalar)
def elementwise_matrix_multiplication(mat1, mat2):
    return np.multiply(mat1, mat2)
def  matrix_multiplication(mat1, mat2):
    return np.dot(mat1, mat2)
def matrix_transpose(mat1):
    return np.transpose(mat1)
def trace_of_matrix(mat1):
    return np.trace(mat1)
def solve_system_of_linear_equations(mat1, mat2):
    return np.linalg.solve(mat1, mat2)
def determinant(mat1):
    return np.linalg.det(mat1)
def inverse(mat1):
    return np.linalg.inv(mat1)
def eigen_value_and_eigen_vector(mat1):
    return np.linalg.eig(mat1)

if __name__ == "__main__":
    
    
    rows1=int(input("Enter the number of rows: "))
    columns1=int(input("Enter the number of columns: "))
    mat1=np.zeros((rows1,columns1))
    for i in range(rows1):
        for j in range(columns1):
            print("Enter the element at position ",i,j)
            mat1[i][j]=int(input())
            
            
    rows2=int(input("Enter the number of rows: "))
    columns2=int(input("Enter the number of columns: "))
    mat2=np.zeros((rows2,columns2))
    for i in range(rows2):
        for j in range(columns2):
            print("Enter the element at position ",i,j)
            mat2[i][j]=int(input())
            
    
    while True:
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Scalar Matrix Multiplication")
        print("4. Elementwise Matrix Multiplication")
        print("5. Matrix Multiplication")
        print("6. Matrix Transpose")
        print("7. Trace of a Matrix")
        print("8. Solve System of Linear Equations")
        print("9. Determinant")
        print("10. Inverse")
        print("11. Eigen Value and Eigen Vector")
        print("12. Exit")
        
        
        option=int(input("Enter your choice: "))
        if (option==1):
            if (rows1!=rows2 or columns1!=columns2):
                print("Matrix addition is not possible")
                continue
            else:
                mat3= matrix_addition(mat1,mat2)
                printmatrix(mat3)
        elif (option==2):
            if (rows1!=rows2 or columns1!=columns2):
                print("Matrix subtraction is not possible")
                continue
            else:
                mat3= matrix_subtraction(mat1,mat2)
                printmatrix(mat3)
        elif (option==3):
            
            value=int(input("Enter the scalar value: "))
            mat3= scalar_matrix_multiplication(mat1,value)
            printmatrix(mat3)
        elif (option==4):
            if (rows1!=rows2 or columns1!=columns2):
                print("Elementwise matrix multiplication is not possible")
                continue
            else:
                mat3= elementwise_matrix_multiplication(mat1,mat2)
                printmatrix(mat3)
        elif (option==5):
            if (columns1!=rows2):
                print("Matrix multiplication is not possible")
                continue
            else:
                mat3= matrix_multiplication(mat1,mat2)
                printmatrix(mat3)
        elif (option==6):
            mat3= matrix_transpose(mat1)
            printmatrix(mat3)
        elif (option==7):
          print(trace_of_matrix(mat1))
        
        elif (option==8):
            rows1=int(input("Enter the number of rows: "))
            columns1=int(input("Enter the number of columns: "))
            mat1=np.zeros((rows1,columns1))
            for i in range(rows1):
                for j in range(columns1):
                    print("Enter the element at position ",i,j)
                    mat1[i][j]=int(input())
            
            
            rows2=int(input("Enter the number of rows: "))
            columns2=int(input("Enter the number of columns: "))
            mat2=np.zeros((rows2,columns2))
            for i in range(rows2):
                 for j in range(columns2):
                    print("Enter the element at position ",i,j)
                    mat2[i][j]=int(input())
            
            if(rows2!=rows1 or columns1!=1):
                print("System of linear equations cannot be solved")
                continue
            else:
                mat3= solve_system_of_linear_equations(mat1,mat2)
                printmatrix(mat3)
        elif (option==9):
            print(determinant(mat1))
           
        elif (option==10):
            if(determinant(mat1)==0):
                print("Inverse of the matrix does not exist")
                continue
            else:
                mat3= inverse(mat1)
                printmatrix(mat3)
            
        elif (option==11):
            mat3,mat4= eigen_value_and_eigen_vector(mat1)
            print(mat3)
            print(mat4)
            
        elif (option==12):
            exit()
            
            
        else:
         print("Invalid option")
         
         
            
            
            
            
           
            
        




