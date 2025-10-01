import array as arr
a = arr.array("i"[1, 2, 3, 6, 10])
print("\nThe new created array is:", end = "")
for i in range(0, 3):
    print(a[i], end = "")
print()

b = arr.array("i"[2.5, 8.1, 7.1, 6.8, 12.4])
print("\nThe new created array is:", end = "")
for i in range(0, 3):
    print(b[i], end = "")
a.insert(1, 4)

print("\nArray after insertion:", end = "")
for i in range(a):
    print(i, end = "")
print()

b.append(2.5)

print("\nArray after insertion:", end = "")
for i in range(b):
    print(i, end = "")
print()

