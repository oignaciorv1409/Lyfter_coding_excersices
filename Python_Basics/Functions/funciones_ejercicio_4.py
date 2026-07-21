temp_list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def to_sum_list_of_numbers (temp_list_numbers):
        total = 0

        for number in temp_list_numbers:
                total += number

        return total

result = to_sum_list_of_numbers(temp_list_numbers)
print(result)