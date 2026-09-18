print("==============================")
print("   STUDENT GRADE CALCULATOR".center(40))
print("==============================")

name = input("What is your name? ")

python_mark = int(input("Enter your Python mark: "))
networking_mark = int(input("Enter your Networking mark: "))
mathematic_mark = int(input("Enter your Mathematic mark: "))

total_mark = python_mark + networking_mark + mathematic_mark
average = total_mark / 3

print("Hello", name)
print("Your total mark is:", total_mark)

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

print("\n==== RESULTS ====")
print("Name:", name)
print("Total Mark:", total_mark)
print("Average:", average)
print("Grade:", grade) 