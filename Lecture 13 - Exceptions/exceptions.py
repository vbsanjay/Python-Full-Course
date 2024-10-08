# num1 = 10
# num2 = 0
# try:
#     res = num1 / num2
#     print(res)
# except ZeroDivisionError as e:
#     print(e)


# def check_positive(number):
#     try:
#         if number < 0:
#             raise ValueError("Negative number!")
#     except ValueError as e:
#         print(f"Caught an exception: {e}")
#         raise  # Re-raises the caught exception

# check_positive(-1)

class CustomError(Exception):
    """Base class for custom exceptions."""
    def __init__(self, message="Something went wrong"):
        self.message = message
        super().__init__(self.message)


def process_data(value):
    if value < 0:
        raise CustomError("Negative value is not allowed.")
    return value


def wrapper():
    try:
        process_data(-1)
    except CustomError as e:
        print(f"Handling custom exception: {e}")
        raise  # Re-raises the caught custom exception

try:
    wrapper()
except CustomError as e:
    print(f"Re-raised custom exception: {e}")
