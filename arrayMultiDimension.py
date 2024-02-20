arrayValues = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valueLength = len(arrayValues)

for i in arrayValues:
    firstValue = i[1]
    lastValue = i[valueLength - 1]
    # print(f"array firstValue = {firstValue}")
    # print(f"arrayLastValue = {lastValue}")

    # if lastValue > 0:
    #     print(f"{firstValue * lastValue}")



scores = [
    {'studentID': 0, 'm': 85, 's': 90, 'e': 95},   # Student 1 scores: Math=85, Science=90, English=95
    {'studentID': 1, 'm': 70, 's': 75, 'e': 80},   # Student 2 scores: Math=70, Science=75, English=80
    {'studentID': 2, 'm': 95, 's': 85, 'e': 90}    # Student 3 scores: Math=95, Science=85, English=90
]

def get_student_details_by_id(student_id):
    for student in scores:
        if student['studentID'] == student_id:
            print(student)
            return student
    return None

# Example: Get details of student with ID 1
student_id = 2
student_details = get_student_details_by_id(student_id)
if student_details:
    print("Details of student with ID", student_id, ":", student_details)
else:
    print("Student with ID", student_id, "not found.")

