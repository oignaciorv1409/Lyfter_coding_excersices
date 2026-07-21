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



avg_approved = sum_approved / count_approved
if avg_approved >= 70:
        print(f"Your average is approved with: {avg_approved}")

avg_disapproved = sum_disapproved / count_disapproved
if avg_disapproved > 70:
        print(f"Your average is dissaproved with: {avg_disapproved}")

avg_total = sum_total / grades
if avg_total > 70:
        print(f"Average approved! :) your final avg grade is: {avg_total}")
elif avg_total < 70:
        print(f"Average Disapproved...  :( your final avg grade is: {avg_total}")