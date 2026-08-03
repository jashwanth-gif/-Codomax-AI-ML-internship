import numpy as np

print("numpy basics")

a = np.array([10, 20, 30, 40, 50])
print("a =", a)

print("shape:", a.shape)
print("size:", a.size)
print("dimensions:", a.ndim)
print("type:", a.dtype)

print("first:", a[0])
print("last:", a[-1])

print("slice1:", a[:3])
print("slice2:", a[1:4])

b = np.array([1, 2, 3, 4, 5])
print("b =", b)

print("add:", a + b)
print("sub:", a - b)
print("mul:", a * b)
print("div:", a / b)

print("sum:", np.sum(a))
print("mean:", np.mean(a))
print("max:", np.max(a))
print("min:", np.min(a))

c = np.array([1, 2, 3, 4, 5, 6])
print("reshape:")
print(c.reshape(2, 3))

d = np.array([[1, 2, 3], [4, 5, 6]])
print("2d array:")
print(d)

print("first row:", d[0])
print("second column:", d[:, 1])
print("transpose:")
print(d.T)

e = np.array([7, 8, 9])
f = np.array([10, 11, 12])

print("concat:", np.concatenate((e, f)))
print("stack:")
print(np.stack((e, f)))

g = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("split:")
print(np.split(g, 2))

print("greater than 25:", a > 25)
print("filtered:", a[a > 25])