all_grades = 0
current_grade = 0
sum_total = 0
sum_approved = 0
sum_disapproved = 0
count_approved = 0
count_disapproved = 0 

grades = int(input("How many grades are you checking?"))

for all_grades in range(grades):
        current_grade = float(input("Please enter the grade: "))
        sum_total += current_grade

        if current_grade >= 70:
                print("Approved!")
                count_approved += 1
                sum_approved += current_grade
        
        else:
                print("Disapproved!")
                count_disapproved += 1
                sum_disapproved += current_grade



if count_approved > 0:
        avg_approved = sum_approved / count_approved
        print(f"Your average approved grade is: {avg_approved}")
        print(f"You have approved {count_approved} grades")
else:
        print("You have 0 approved grades, so approved average cannot be calculated.")


if count_disapproved > 0:
        avg_disapproved = sum_disapproved / count_disapproved
        print(f"Your average disapproved grade is: {avg_disapproved}")
        print(f"You have failed {count_disapproved} grades")
else:
        print("You have 0 disapproved grades, so disapproved average cannot be calculated.")

avg_total = sum_total / grades
if avg_total >= 70:
        print(f"Average approved! :) your final grade is: {avg_total}")
if avg_total < 70:
        print(f"Average Disapproved...  :( your final grade is: {avg_total}")