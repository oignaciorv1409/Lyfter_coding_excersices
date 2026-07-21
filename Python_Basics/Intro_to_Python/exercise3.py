import random
secret_number = random.choice([1,2,3,4,5,6,7,8,9,10]) # Random number will be pick up from list "secret_numbers"
user_input = 0

# print(secret_number) # Print to check out random elements are working as expected 

while True:
        user_input = int(input("Pick up a number between 1 to 10: "))
        
        if user_input == secret_number:
                print(f"Congrats you pick the right number! The secret number is  {secret_number}.")
                break
        else:
                print("Nope... Try again")