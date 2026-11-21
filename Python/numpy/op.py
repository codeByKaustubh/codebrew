
import numpy as np

print("=" * 50)
print("       NUMPY BASIC TO ADVANCED")
print("=" * 50)

# 1. ARRAY CREATION
print("\n1. ARRAY CREATION")

a = np.array([10, 20, 30, 40, 50])
b = np.array([[10, 20, 30],
              [40, 50, 60]])

print("1D Array:", a)
print("2D Array:\n", b)

print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((2, 3)))
print("Full:", np.full((2, 2), 7))
print("Arange:", np.arange(1, 11))
print("Linspace:", np.linspace(1, 10, 5))
print("Identity:\n", np.eye(3))
print("Diagonal:", np.diag([10, 20, 30]))

# 2. ARRAY ATTRIBUTES
print("\n2. ARRAY ATTRIBUTES")

print("Dimensions:", b.ndim)
print("Shape:", b.shape)
print("Size:", b.size)
print("Data Type:", b.dtype)
print("Item Size:", b.itemsize)
print("Memory:", b.nbytes)
print("Transpose:\n", b.T)

# 3. DATA TYPES
print("\n3. DATA TYPES")

c = np.array([10, 20, 30], dtype=np.float64)
print("Float Array:", c)
print("Data Type:", c.dtype)
print("Convert Integer:", c.astype(np.int32))

# 4. INDEXING AND SLICING
print("\n4. INDEXING AND SLICING")

print("First:", a[0])
print("Last:", a[-1])
print("Slicing:", a[1:4])
print("Reverse:", a[::-1])
print("Every Second:", a[::2])

# 5. MATHEMATICAL OPERATIONS
print("\n5. MATHEMATICAL OPERATIONS")

x = np.array([10, 20, 30])
y = np.array([2, 4, 5])

print("Addition:", np.add(x, y))
print("Subtraction:", np.subtract(x, y))
print("Multiplication:", np.multiply(x, y))
print("Division:", np.divide(x, y))
print("Power:", np.power(x, 2))
print("Square:", np.square(x))
print("Square Root:", np.sqrt(x))
print("Absolute:", np.abs([-10, -20, 30]))
print("Modulus:", np.mod(x, y))
print("Round:", np.round([1.25, 2.56], 1))
print("Floor:", np.floor([1.8, 2.9]))
print("Ceil:", np.ceil([1.2, 2.1]))

# 6. STATISTICAL FUNCTIONS
print("\n6. STATISTICAL FUNCTIONS")

marks = np.array([45, 60, 75, 80, 90, 95])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Sum:", np.sum(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))
print("Percentile:", np.percentile(marks, 50))
print("Quantile:", np.quantile(marks, 0.5))
print("Argmin:", np.argmin(marks))
print("Argmax:", np.argmax(marks))
print("Cumulative Sum:", np.cumsum(marks))
print("Cumulative Product:", np.cumprod(marks))

# 7. ARRAY MANIPULATION
print("\n7. ARRAY MANIPULATION")

d = np.arange(1, 13)

print("Original:", d)
print("Reshape:\n", d.reshape(3, 4))
print("Flatten:", d.reshape(3, 4).flatten())
print("Ravel:", d.reshape(3, 4).ravel())
print("Transpose:\n", d.reshape(3, 4).transpose())

e = np.array([10, 20, 30])
print("Expand:", np.expand_dims(e, axis=0))

f = np.array([[10, 20, 30]])
print("Squeeze:", np.squeeze(f))

# 8. JOINING AND SPLITTING
print("\n8. JOINING AND SPLITTING")

p = np.array([10, 20, 30])
q = np.array([40, 50, 60])

print("Concatenate:", np.concatenate((p, q)))
print("Stack:\n", np.stack((p, q)))
print("Vertical:\n", np.vstack((p, q)))
print("Horizontal:", np.hstack((p, q)))

print("Split:", np.split(np.arange(1, 7), 3))
print("Array Split:", np.array_split(np.arange(1, 8), 3))

# 9. SEARCHING AND SORTING
print("\n9. SEARCHING AND SORTING")

values = np.array([50, 20, 40, 10, 30, 20])

print("Sort:", np.sort(values))
print("Argsort:", np.argsort(values))
print("Unique:", np.unique(values))
print("Where:", np.where(values > 30))
print("Nonzero:", np.nonzero(values))
print("Isin:", np.isin(values, [20, 40]))
print("Extract:", np.extract(values > 30, values))
print("Argwhere:", np.argwhere(values > 30))

# 10. BOOLEAN FILTERING
print("\n10. BOOLEAN FILTERING")

print("Passed:", marks[marks >= 40])
print("Distinction:", marks[marks >= 75])
print("Failed:", marks[marks < 40])

# 11. RANDOM NUMBERS
print("\n11. RANDOM NUMBERS")

rng = np.random.default_rng(42)

print("Random:", rng.random(5))
print("Integers:", rng.integers(1, 100, size=5))
print("Normal:", rng.normal(0, 1, size=5))
print("Choice:", rng.choice([10, 20, 30, 40], size=3))

random_array = np.array([10, 20, 30, 40, 50])
rng.shuffle(random_array)

print("Shuffle:", random_array)
print("Permutation:", rng.permutation([1, 2, 3, 4, 5]))

# 12. MATRIX OPERATIONS
print("\n12. MATRIX OPERATIONS")

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Addition:\n", m1 + m2)
print("Multiplication:\n", m1 @ m2)
print("Dot Product:\n", np.dot(m1, m2))
print("Inverse:\n", np.linalg.inv(m1))
print("Determinant:", np.linalg.det(m1))
print("Eigenvalues:", np.linalg.eig(m1)[0])
print("Rank:", np.linalg.matrix_rank(m1))
print("Trace:", np.trace(m1))

# 13. BROADCASTING
print("\n13. BROADCASTING")

arr = np.array([10, 20, 30])

print("Add 5:", arr + 5)
print("Multiply 2:", arr * 2)

arr2 = np.array([[1], [2], [3]])
print("Broadcasting:\n", arr2 + arr)

# 14. ADVANCED FUNCTIONS
print("\n14. ADVANCED FUNCTIONS")

data = np.array([10, 20, 30, 40, 50])

print("Clip:", np.clip(data, 20, 40))
print("Difference:", np.diff(data))
print("Gradient:", np.gradient(data))
print("Histogram:", np.histogram(data, bins=3))
print("Digitize:", np.digitize(data, bins=[20, 40]))

v1 = np.array([10, 20, 30])
v2 = np.array([20, 30, 40])

print("Correlation:\n", np.corrcoef(v1, v2))
print("Covariance:\n", np.cov(v1, v2))

# 15. CONDITIONAL OPERATIONS
print("\n15. CONDITIONAL OPERATIONS")

nums = np.array([10, 25, 40, 55, 70])

print("Condition:", np.where(nums >= 40, "Pass", "Fail"))
print("Select:", np.select(
    [nums >= 60, nums >= 40],
    ["Good", "Average"],
    default="Low"
))

# 16. COPY AND VIEW
print("\n16. COPY AND VIEW")

original = np.array([10, 20, 30])

copy_array = original.copy()
view_array = original.view()

copy_array[0] = 100

print("Original:", original)
print("Copy:", copy_array)
print("View:", view_array)

# 17. SAVE AND LOAD
print("\n17. SAVE AND LOAD")

np.save("numpy_data.npy", marks)
loaded = np.load("numpy_data.npy")

print("Loaded NPY:", loaded)

np.savetxt("numpy_data.csv", marks, delimiter=",")
print("CSV File Saved")

# 18. STUDENT RESULT ANALYSIS
print("\n18. STUDENT RESULT ANALYSIS")

student_marks = np.array([
    [80, 75, 90],
    [60, 65, 70],
    [45, 50, 55],
    [90, 95, 85]
])

total = np.sum(student_marks, axis=1)
average = np.mean(student_marks, axis=1)

print("Student Marks:\n", student_marks)
print("Total:", total)
print("Average:", average)
print("Highest Average:", np.max(average))
print("Lowest Average:", np.min(average))

print("\n===== NUMPY PROGRAM COMPLETED =====")
