
"""
Dictionary Comprehensions - helps transform one dictionary to another
`for in` indicates it could be good use case where dictionary comprehension can be applied to simplify code
"""

student_grades = {
    "A": [84, 56, 67],
    "B": [78, 89, 90],
    "C": [23, 56, 67],
}

by_grade_avg = { name: sum(grades)/len(grades) for name, grades in student_grades.items()}
nums_and_cubes = { i : i**3 for i in range(1, 6)}

print(by_grade_avg)
print(nums_and_cubes)