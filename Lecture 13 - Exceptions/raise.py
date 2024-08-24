# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
# def get_integer():
#     try:
#         user_input = input("Please enter an integer: ")
#         user_input = int(user_input)  # Attempt to convert the input to an integer
#         print(f"Valid integer entered: {user_input}")
#     except ValueError:
#         raise ValueError("Invalid input. You must enter a valid integer.")

# # Call the function
# get_integer()

# How can you catch multiple exceptions in a single except block?
def perform_division(num1, num2):
    try:
        result = num1//num2
        print(result)
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error:  {e}")

perform_division(1,2)
perform_division(2,0)
perform_division("3",2)

# How do you create a custom exception in Python?

class MyCustomException(Exception):
    pass
    # should check numbers are less than 10

def check_number(*nums):
    try:
        for num in nums:
            int(num)
        print("Valid inputs")
    except MyCustomException as e:
        print(f"Error:  {e}")

