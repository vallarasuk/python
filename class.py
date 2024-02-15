# Adding elements to an array
my_array = [1, 2, 3, 4]

# Appending element at the end
my_array.append(5)
print(my_array)  # Output: [1, 2, 3, 4, 5]

# Inserting element at index 2
my_array.insert(-len(my_array) ,0)
print(-len(my_array))
print(my_array)  # Output: [1, 2, 10, 3, 4, 5]
