l = [4, 1, 5, 6, 9, 7, 4, 2]
print("Original list:", l)
count = 0
for i in l:
    count += i
    
avg = count/len(l)
print("sum =", count)
print("average =", avg)
l.sort()
print("the sorted list is:", l)
print("Smallest element is:", l[0])
print("Largest element is:", l[-1])
print("range =", l[-1]-l[0])