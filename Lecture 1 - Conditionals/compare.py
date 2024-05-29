x = int(input("What's x?: "))
y = int(input("What's y?: "))

# basic condition statement
if x == y:
    print("x is equal to y")
elif x < y:
    print("x is lesser than y")
else:
    print("y is lesser than x")

# chained comparison
if 5 < x < 10:
    print("x is inbetween 5 and 10")

# and operator
if x > 10 and y > 10:
    print("x and y are greater than 10")

# or operator
if x % 2 == 0 or y % 2 == 0:
    print("either x or y is even")


# ternary conditional expression or ternary operator
def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print("Given number is even")


def is_even(num):
    return True if num % 2 == 0 else False


main()

# match
name = input("what is your name? ")

match name:
    case "harry" | "ron" | "hermione" | "sanjay":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("who?")
