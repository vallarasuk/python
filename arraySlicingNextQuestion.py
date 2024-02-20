# Problem 11: Counting Negative Numbers
numbers = [-2, -1, 0, 1, 2, 3, -4, -5, -6]
negativeNumber = []

for number in numbers:
    if number < 0:
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
palindromeString = []
for word in words:
    if word == word[::-1]:
        palindromeString.append(word)
print(f"palindromeString Number --> {palindromeString}")


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

subReversedValue = []
for value in subLists:
    subReversedValue.append(value[::-1])

print(f"subReversedValue -->  {subReversedValue}")

# Problem 19: Checking Prime Numbers
primeNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Prime Status: [True, True, False, True, False, True, False, False, False]
primeNumberValue = []
for number in primeNumbers:
    if number > 1:
        is_prime = True
        for i in range(2, number):  # Iterate from 2 to number - 1
            if number % i == 0:
                is_prime = False
                break
        primeNumberValue.append(is_prime)
    else:
        primeNumberValue.append(False)

print(f"Prime Status: {primeNumberValue}")


# Problem 20: Finding Common Elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
sameValue = []
for num in list1:
    if num in list2:
        sameValue.append(num)
print(f"sameValue --> {sameValue}")
