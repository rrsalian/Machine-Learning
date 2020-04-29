import numpy as np;

ar=np.array([1,2,3])

ar=np.array([(1,2,3),(3,4,5)],dtype=float)
# print(ar)

ar = np.array([(1, 2, 3), (3, 4, 5),(6,7,8)], dtype=float)

# print(ar)

#Creating Zero
print(np.zeros((2,3)))

print(np.ones((3,3),dtype=np.int16))

print(np.arange(2,10,2))

print(np.linspace(1,10,10))

print(ar.T) #Transpose

arT=ar.T

#Dot mul
print(ar.dot(arT))

""" Determinet of upper triangle matrix is product of diagnal element """

a = np.array([(2, 3, 4), (0, 2, 5), (0, 0, 2)])
# a
# array([[2, 3, 4],
#        [0, 2, 5],
#        [0, 0, 2]])
np.linalg.det(a)
# 7.999999999999998

""" Determinet of row exhanged matrix will change the sign """

a=np.array([(2, 3, 4), (0, 0, 2), (0, 2, 5)])
np.linalg.det(a)
# - 7.999999999999998
