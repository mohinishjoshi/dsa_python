from array import *

# Creation
arr = array('i', [1, 2, 3, 4, 5])
print(arr)

# Insertion
# 1. Append a particular element
arr.append(1)
print(arr)

# 2. Add the contents of 1 arr to another.
arr.extend([3,2])
print(arr)

# 3. Insert an element at an index.
arr.insert(1, 23)
print("Insert", arr)

# Update
arr[0] = -1
print(arr)

# Delete

# 1. Pop - Remove and return last element
print("Popping", arr.pop())
print(arr)


# 2. Remove - Delete a particular element's 1st occurrence from the array
arr.remove(-1)
print(arr)

# 3. Del - Delete a particular element.
del arr[0]
print(arr)

# Array Traversal

