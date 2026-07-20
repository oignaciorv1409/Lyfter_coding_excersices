first_number = int(input('Please enter the first number: '))
second_number = int(input('Please enter the second number: '))
third_number = int(input('Please enter the third number: '))


if first_number > second_number and first_number > third_number:
        print(f"{first_number} is greater than {second_number} and {third_number}.")

elif second_number > first_number and second_number > third_number:
        print(f"{second_number} is greater than {first_number} and {third_number}.")

else:
        print(f"{third_number} is greater than {first_number} and {second_number}.")