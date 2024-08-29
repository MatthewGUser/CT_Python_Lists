# [ Task 1 ]

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()  # Sorts the list in place
# Convert list to string for concatenation
print("Previous:\n" + str(grades))
print("Sorted:\n" + str(grades))    

# [ Task 2 ]

total_sum = sum(grades)

average = total_sum / len(grades)
print("Average is: " + str(average))
