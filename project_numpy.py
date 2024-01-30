import numpy as np
#Array with fixed element
#A one-dimensional element with 5 zeros and ones
# A=np.zeros(5)
# print("A: ",A)
# print("__________________________________")
# a=np.ones(10)
# print("a: ",a)

# #Multidimensional element
# print("__________________________________")
# B=np.zeros((3,4))
# print("B: ")
# print(B)
# print("__________________________________")
# b=np.ones((5,5))
# print("b: ")
# print(b)
# print("__________________________________")
# data=np.ones(4)
# print(data.dtype)
# print("__________________________________")
# data=np.ones(4,dtype=np.int32)
# print(data.dtype)
# print("__________________________________")
# X1=8.3*np.ones(15)
# print(X1)
# print("__________________________________")

# #Array with specific element or multiplication
# x2=np.full(15,8.3)
# print(x2)
# print("__________________________________")
# x3=np.full((4,3),8.3)
# print(x3)
# print("__________________________________")

# #Empty array, fill it
# x4=np.empty(5)
# x4.fill(6.9)
# print(x4)
# print("__________________________________")

# #Useful functions
# print(np.arange(0,10,1))
# print(np.arange(2))
# print(np.arange(0))
# print(np.arange(1,11,3))
# print("__________________________________")
# print(np.linspace(0,10,11))
# print(np.linspace(0,10))
# print(np.linspace(0,10,11,endpoint=False))

# #Order for logarithmic arrays
# print(np.logspace(0,3,20))#20 data ponits between 10**0=1 to 10**3=1000
# print(np.logspace(0,3,20,base=3))

# #Multidimensional coordinate grids
# x=np.array([-1,0,1])
# y=np.array([-2,0,2])
# x,y=np.meshgrid(x,y)
# print(x)
# print(y)
# print("__________________________________")
# x=np.array([-1.5,-1,-0.5,1,1,1.5])
# y=np.array([-2,-1,0,1,2])
# x,y=np.meshgrid(x,y)
# print(x)
# print(y)
# print("__________________________________")
# z=(x+y)**2
# print(z)

#Arrays that are not initialized
#print(np.empty(10,dtype=np.float_))

#An array that takes properties from other arrays
# def f(x):
#     y=np.ones_like(x)
#     return y
# x=np.array([1,5,8,9,12],dtype=complex)
# print(f(x))

#Constructing matrices
# print(np.identity(5))
# print(np.eye(5,k=0))# k = Diameter
# print(np.eye(5,k=4))
# #Data on diameter
# print(np.diag(np.arange(0,27,5)))