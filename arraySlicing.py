# Problem 1: Extracting Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = []
for i in numbers:
    if i % 2 == 0:
        evenNumbers.append(i)
print(f"Even Number Value = {evenNumbers}")

# Problem 2: Reversing Strings
words = ["apple", "banana", "cherry", "date"]
reversedWords = []
# append method
for i in words:
    reversedWords.append(i[::-1])
print(reversedWords)

# insert method
for i in words:
    reversedWords.insert(0, [i[::-1]])
print(reversedWords)

# #########Problem 3: Extracting Subarray
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
outputMatrix = []
for value in matrix:
    outputMatrix.append(value[1:])
print(outputMatrix)

# Problem 4: Squaring Positive Numbers
squareNumbers = [-2, -1, 0, 1, 2, 3, 4, 5]
positiveNumber = []

for number in squareNumbers:
    if number >= 0:
        positiveNumber.append(number ** 2)
print(positiveNumber)

# Problem 5: Extracting First and Last Elements
elements = [10, 20, 30, 40, 50]

firstAndLastElement = [elements[0], elements[-1]]
print(firstAndLastElement)

# Problem 6: Merging Sub arrays

subArray = [[1, 2], [3, 4], [5, 6], [7, 8]]
sumArrayValue = []
for value in subArray:
    sumArrayValue = sumArrayValue + value
print(sumArrayValue)

# Problem 7: Finding Maximum in Sub arrays
matrixValue = [[3, 2, 1], [4, 5, 6], [9, 8, 7]]

maxMatrixValue = []

for sublist in matrixValue:
    maxMatrixValue.append(max(sublist))

print(maxMatrixValue)

# Problem 8: Extracting Odd Numbers

unNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddNumber = []
for num in unNum:
    if num % 2 != 0:
        oddNumber.append(num)
print(oddNumber)

# Problem 9: Flattening Sub arrays

flatMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenSubarray = []
for value in flatMatrix:
    flattenSubarray += value
print(flattenSubarray)

# Problem 10: Extracting Middle Element

randomNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
middleNumber = len(randomNumbers) // 2
exactedMiddleNumber = randomNumbers[middleNumber]
print(exactedMiddleNumber)

# Computer solved Answer Method

# Problem 1: Extracting Even Numbers (List Comprehension)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = [num for num in numbers if num % 2 == 0]
print(f"Even Numbers: {evenNumbers}")

# Problem 2: Reversing Strings (List Comprehension)
words = ["apple", "banana", "cherry", "date"]
reversedWords = [word[::-1] for word in words]
print(f"Reversed Words: {reversedWords}")

# Problem 3: Extracting Sub arrays (List Comprehension)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
outputMatrix = [row[1:] for row in matrix]
print(f"Output Matrix: {outputMatrix}")

# Problem 4: Squaring Positive Numbers (List Comprehension)
squareNumbers = [-2, -1, 0, 1, 2, 3, 4, 5]
positiveSquares = [num ** 2 for num in squareNumbers if num >= 0]
print(f"Positive Squares: {positiveSquares}")

# Problem 5: Extracting First and Last Elements (Slice Notation)
elements = [10, 20, 30, 40, 50]
firstAndLastElement = elements[::len(elements) - 1]
print(f"First and Last Element: {firstAndLastElement}")

# Problem 6: Merging Sub arrays (List Comprehension)
subArray = [[1, 2], [3, 4], [5, 6], [7, 8]]
sumArrayValue = [num for sublist in subArray for num in sublist]
print(f"Sum Array Value: {sumArrayValue}")

# Problem 7: Finding Maximum in Sub arrays (List Comprehension)
matrixValue = [[3, 2, 1], [4, 5, 6], [9, 8, 7]]
maxMatrixValue = [max(sublist) for sublist in matrixValue]
print(f"Max Matrix Value: {maxMatrixValue}")

# Problem 8: Extracting Odd Numbers (List Comprehension)
unNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddNumbers = [num for num in unNum if num % 2 != 0]
print(f"Odd Numbers: {oddNumbers}")

# Problem 9: Flattening Sub arrays (List Comprehension)
flatMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenSubarray = [num for sublist in flatMatrix for num in sublist]
print(f"Flattened Subarray: {flattenSubarray}")

# Problem 10: Extracting Middle Element (Slice Notation)
randomNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
middleNumber = randomNumbers[len(randomNumbers) // 2]
print(f"Middle Number: {middleNumber}")
