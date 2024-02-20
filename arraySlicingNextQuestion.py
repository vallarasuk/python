# Problem 11: Counting Negative Numbers
numbers = [-2, -1, 0, 1, 2, 3, -4, -5, -6]
negativeNumber = []

for number in numbers:
    if number % 2:
        negativeNumber.append(number)

print(f"negativeNumber --> {negativeNumber}")
print(f"Negative Number Length --> {len(negativeNumber)}")

# Problem 12: Filtering Strings by Length
words = ["apple", "banana", "cherry", "date", "grape", "kiwi"]
greaterThanFiveValue = []

for word in words:
    if len(word) > 5:
        greaterThanFiveValue.append(word)
print(f"value --> {greaterThanFiveValue}")
print(f"length --> {len(greaterThanFiveValue)}")

# Problem 13: Sum of Squares
randomNumbers = [1, 2, 3, 4, 5]
totalRandomNumValue = []
for ranNum in randomNumbers:
    subTotal = totalRandomNumValue.append(ranNum ** 2)

print(f"total Random number value --> {sum(totalRandomNumValue)}")

# Problem 14: Extracting Digits
randomDigits = [123, 456, 789]
extractDigits = []
for ran in randomDigits:
    num_count = str(ran)
    for i in num_count:
        extractDigits.append(int(i))

print(f"extractDigits  --> {extractDigits}")


# Problem 15: Checking Palindrome Strings

words = ["level", "hello", "radar", "python"]

# for word in words:
    # print(word)


# Problem 16: Removing Duplicates

duplicateRanNum = [1, 2, 3, 4, 2, 5, 6, 3]
removedDuplicateNum = []

for num in duplicateRanNum:
    if num not in removedDuplicateNum:
        removedDuplicateNum.append(num)
print(f"Removed Duplicate Value --> {removedDuplicateNum}")

# Problem 17: Counting Vowels

vowelsWords = ["apple", "banana", "cherry", "date"]

vowelsWordsList = ["a,e,i,o,u,y"]
vowelsWordsLength = []


# Problem 18: Reversing Sublist
subLists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Problem 19: Checking Prime Numbers
primeNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]


# Problem 20: Finding Common Elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

for num in list1:

    print(num)
