import numpy as np

# x = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

# print(np.diag(x));

# print(np.array([1, 4, 8])[[True, False, True]])

# x = np.array([1, 2, 0, 2, 0, 0, 4, 5, 0, 6])
# print(x)
# y = np.argwhere(x == 0) + 1;
# print(y)
# y = y[y < len(x)]
# ans = (np.take(x, y)).max()
# print(ans)

x = np.array([1, 1, 1, 5, 5, 5, 6, 7, 7, 7, 5, 5])
a = np.diff(x)
a = np.argwhere(a == 0)
print(a)
# a = np.reshape(a, -1)
# print(a)