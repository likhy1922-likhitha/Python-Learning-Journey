import numpy as np

# linalg is a NumPy sub-module for linear algebra
# It is used to find determinant, inverse, eigenvalues, etc.
# t find means satisifes a*d-b*c=determinant
determinant = np.linalg.det([[1, 2], [2, 1]])
print(determinant)
# to find the eigen values and eigen vectors
values, vectors = np.linalg.eig([[1,2],[2,1]])
print(values)
print(vectors)
# to find the inverse of a matrix  remember if determinant = 0 then cant find the inverse
inverse = np.linalg.inv([[1,2],[2,1]])
print(inverse)
