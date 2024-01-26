from scipy import linalg as la
from scipy import optimize
import sympy
import numpy as np
import matplotlib.pyplot as plt
#A=sympy.Matrix([[2,3],[5,4]])
#b=sympy.Matrix([4,3])
#L,U,_ =A.LUdecomposition()
#print(L,U,_)
#print(L*U)
#x=A.LUsolve(b)
#print(x)

#print("rank : ",A.rank())
#print("condition_number :",A.condition_number())
#print("norm :",A.norm())

#A=np.array([[2,3],[5,4]])
#b=np.array([4,3])
#print("rank : ",np.linalg.matrix_rank(A))
#print("condition_number :",np.linalg.cond(A))
#print("norm :",np.linalg.norm(A))


A=np.array([[2,3],[5,4]])
b=np.array([4,3])
#Upper triangular and lower triangular matrix
P,L,U=la.lu(A)
print("lower triangular : ")
print(L)
print("Upper triangular : ")
print(U)
print(" or :",P.dot(L.dot(U)))
print(" or :",la.solve(A,b))