# prompt_message = "Please enter a number:  "


def get_number (prompt_text):
        while True:
                try:
                        message = input(prompt_text)
                        user_number = float(message)

                        return user_number
                
                except ValueError:
                        print ("Error: Please enter a valid number.")

# result_user_input = get_number(prompt_message)
# print(result_user_input)


def get_user_option ():
        menu = { 
                "1": "Add",
                "2": "Substract",
                "3": "Multiply",
                "4": "Divide",
                "5": "Delete Result",
                "6": "Exit"
        }

        while True:
                print("\nMenu:")
                for key, value in menu.items():
                        print(f"{key}. {value}")

                user_option = input("Please choose an option: ")

                if user_option in menu:
                        return user_option
                
                else:
                        print("Error: Please choose a valid option in menu.")


def calculate (user_number, user_option, new_number):

        if user_option == "1":
                return user_number + new_number

        elif user_option == "2":
                return user_number - new_number

        elif user_option == "3":
                return user_number * new_number

        elif user_option == "4":
                try:
                        return user_number / new_number
                except ZeroDivisionError:
                        print("Error Division by Zero: Please enter a valid number.")
                        return user_number


def main():
        current_number = get_number("Please enter the starting number: ")

        while True:
                print(f"Curent number: {current_number}")

                current_option = get_user_option()

                if current_option in ("1", "2", "3", "4"):

                        new_number = get_number ("Please enter a number: ")
                        current_number = calculate(current_number, current_option, new_number)
                        pass

                elif current_option == "5":
                        current_number = 0
                        pass

                elif current_option == "6":
                        print ("Goodbye!")
                        break

main()
