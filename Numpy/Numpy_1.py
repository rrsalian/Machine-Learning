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