import numpy as np

""" Determinant of upper triangle or diagnal matrix is product of diagnal element """
a = np.array([(2, 3, 4), (0, 2, 5), (0, 0, 2)])
# array([[2, 3, 4],
#        [0, 2, 5],
#        [0, 0, 2]])

print(np.linalg.det(a))
# 7.999999999999998

""" Determinant of row exhanged matrix will change the sign """
a = np.array([(2, 3, 4), (0, 0, 2), (0, 2, 5)])
print(np.linalg.det(a))
# - 7.999999999999998

""" Determinant of identiy matrix is 1 """
a = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
print(np.linalg.det(a))
# 1

""" Determinant of zero row contain matrix is 0 """
a = np.array([(2, 3, 4), (0, 0, 0), (9, 2, 5)])
print(np.linalg.det(a))
# 0

""" Determinant of singular (dependent column) matrix is 0 """
a = np.array([( 2, 6,  4 ),
              ( 6, 18, 12), 
              ( 9, 27, 5 )])
print(np.linalg.det(a))
# 0

""" Determinant of non-singular (independent column) matrix is non zero """
a = np.array([(2, 6, 4), (6, 7, 12), (9, 9, 5)])
print(np.linalg.det(a))
# 285.99999999999994
