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