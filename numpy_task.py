import numpy as np

a = np.array([[4, 8, 15], [16, 23, 42]])
print('Shape:', a.shape)
print('Second column:', a[:, 1])
print('Column means:', a.mean(axis=0))
print('Doubled array:\n', a * 2)
print('Values greater than 10:', a[a > 10])
