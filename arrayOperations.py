
# Certainly! Let's explain each DSA-level array operation with examples:

# 1. Insertion:
# Insertion refers to adding elements to an array. In Python, you can insert elements at the end of the array using the append() method or at a specific index using the insert() method.

# Adding elements to an array
my_array = [1, 2, 3, 4]

# Appending element at the end
my_array.append(5)
print(my_array)  # Output: [1, 2, 3, 4, 5]

# Inserting element at index 2
my_array.insert(2, 10)
print(my_array)  # Output: [1, 2, 10, 3, 4, 5]




# 2. Deletion:
# Deletion involves removing elements from an array. You can delete elements by their value using the remove() method or by their index using the pop() method.

# Removing element by value
my_array.remove(3)
print(my_array)  # Output: [1, 2, 10, 4, 5]

# Removing element by index
removed_element = my_array.pop(2)
print(removed_element)  # Output: 10
print(my_array)         # Output: [1, 2, 4, 5]



# 3. Search:
# Search operation involves finding elements in an array. You can use the index() method to find the index of an element.

# Searching for an element
index_of_4 = my_array.index(4)
print(index_of_4)  # Output: 2




# 4. Sorting:

# Sorting arranges elements in a specific order. You can use the sorted() function to sort an array.

# Sorting the array
sorted_array = sorted(my_array)
print(sorted_array)  # Output: [1, 2, 4, 5]



# 5. Access:
# Access involves accessing elements at specific indices. You can use indexing to access elements.

# Accessing elements
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 4




# 6. Traversal:
# Traversal involves visiting and processing each element of the array. You can use loops to traverse through the array.

# Traversing the array
for element in my_array:
    print(element)



# 7. Subarrays:
# Subarrays are portions of the array. You can extract subarrays using slicing.

# Extracting subarray
subarray = my_array[1:3]
print(subarray)  # Output: [2, 4]



# 8. Slicing:
# Slicing involves extracting a subset of elements from the array. You can use slicing notation to extract elements.

# Slicing the array
sliced_array = my_array[:3]
print(sliced_array)  # Output: [1, 2, 4]



# 9. Concatenation:
# Concatenation involves joining two arrays together. You can use the + operator to concatenate arrays.

# Concatenating arrays
concatenated_array = my_array + [6, 7]
print(concatenated_array)  # Output: [1, 2, 4, 6, 7]



# 10. Splitting:
# Splitting divides an array into multiple parts. This can be done using slicing.

# Splitting the array
part1 = my_array[:3]
part2 = my_array[2:]
print(part1)  # Output: [1, 2]
print(part2)  # Output: [4, 5]




# 11. Merging:
# Merging combines multiple arrays into one. You can use concatenation or other methods to merge arrays.

# Merging arrays
array1 = [1, 2]
array2 = [3, 4]
merged_array = array1 + array2
print(merged_array)  # Output: [1, 2, 3, 4]