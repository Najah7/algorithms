from array import array

arr = array("i", [1, 2, 3, 4, 5])
print(arr)

import numpy as np

np_arr = np.array([1, 2, 3, 4, 5])
print(np_arr)

# apend element to the end
arr.append(6)

# insert element at the beginning
arr.insert(0, 0)

l = [1, 2, 3, 4, 5]
l2 = l
l3 = l[:]

a = [i for i in range(1, 10)]
print(a[3:0:-1])
