# Grade Calculator

# Get student name
student_name = input("Enter student name: ")

# Get marks for 3 subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Display results

print(f"\nStudent Name: {student_name}")
print(f"Subject 1: {mark1}")
print(f"Subject 2: {mark2}")
print(f"Subject 3: {mark3}")
print(f"Average: {average:.2f}")


# Check pass/fail
if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
